import secrets
import datetime

from argon2 import PasswordHasher
from typing import Annotated

from sqlalchemy import select

from fastapi import Cookie, status, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from backend.src.config import settings
from backend.src.db import SessionDep
from backend.src.models import User, Session


class AuthHandler:
    security_scheme = HTTPBasic()
    ph = PasswordHasher()
    secret = settings.secret_key

    def hash_password(self, password):
        return self.ph.hash(password)

    def verify_password(self, hashed_password, plain_password):
        return self.ph.verify(hashed_password, plain_password)

    async def get_current_user(
            self,
            credentials: Annotated[HTTPBasicCredentials, Depends(security_scheme)],
            db: SessionDep,
    ) -> User:
        pass

    @staticmethod
    async def create_session(
            db: SessionDep,
            user_id: int,
    ) -> str:

        while True:
            session_id = secrets.token_hex(16)
            ttl = datetime.timedelta(hours=settings.session_ttl)
            expires_at = datetime.datetime.now(datetime.UTC) + ttl

            statement = select(Session).where(Session.session_id == session_id)
            existing_session_id = await db.scalar(statement)
            if existing_session_id:
                continue

            session = Session(
                session_id=session_id,
                user_id=user_id,
                expires_at=expires_at,
            )
            db.add(session)
            await db.commit()
            return session_id
    
    async def verify_session(
            self,
            db: SessionDep,
            session_id: str = Cookie(),
    ):
        session = await db.scalar(select(Session).where(Session.session_id == session_id))
        if not session or session.expires_at < datetime.datetime.now(datetime.UTC):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid session',
            )
        return True

