from fastapi import FastAPI

from .config import settings
from .game.router import router as game_router
from .auth.router import router as auth_router

app = FastAPI(title=settings.app_name)

app.include_router(game_router)
app.include_router(auth_router)
