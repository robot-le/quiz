from typing import Annotated
from sqlalchemy import select

from ..db import SessionDep
from ..models import Session, User
from ..schemas import ResponseBaseWithObject, User as UserSchema
from ..auth.auth import AuthHandler

from fastapi import APIRouter, Cookie, Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials
from fastapi.responses import JSONResponse


router = APIRouter()

auth_handler = AuthHandler()


@router.post('/register', response_model=ResponseBaseWithObject[UserSchema])
async def register(
        user_data: HTTPBasicCredentials,
        db: SessionDep,
):
    statement = select(User).where(User.username == user_data.username)
    existing_user = await db.scalar(statement)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Username is taken',
        )

    hashed_pwd = auth_handler.hash_password(user_data.password)
    db_user = User(
        username=user_data.username,
        password=hashed_pwd,
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return ResponseBaseWithObject[UserSchema](
        detail='User successfully registered',
        obj=UserSchema(
            id=db_user.id,
            username=db_user.username,
        ),
    )


@router.post('/login')
async def login(
        user_data: HTTPBasicCredentials,
        db: SessionDep,
):
    user_obj = await db.scalar(select(User).where(User.username == user_data.username))
    if not user_obj or not auth_handler.verify_password(user_obj.password, user_data.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid credentials',
        )
    session_id = await auth_handler.create_session(db, user_obj.id)
    response = JSONResponse(content={'message': 'Logged in successfully'})
    response.set_cookie(key='session_id', value=session_id, httponly=True)
    return response


@router.post(
    "/logout",
    dependencies=[Depends(auth_handler.verify_session)],
)
async def logout(
        db: SessionDep,
        session_id: str = Cookie(None),
):
    if not session_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    session = await db.scalar(select(Session).where(Session.session_id == session_id))
    await db.delete(session)
    await db.commit()
    response = JSONResponse(content={'message': 'Logged out successfully'})
    response.delete_cookie(key='session_id')
    return response


@router.get('/current-user', response_model=ResponseBaseWithObject[UserSchema])
async def get_current_user(
        user: Annotated[User, Depends(auth_handler.get_current_user)],
):
    return ResponseBaseWithObject[UserSchema](
        detail='User Authenticated',
        obj=UserSchema(
            id=user.id,
            username=user.username,
        ),
    )
