from fastapi import APIRouter

from app.routers import token, user

api_router = APIRouter(prefix="/api/v2")

api_router.include_router(user.router)
api_router.include_router(token.router)
