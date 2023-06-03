from fastapi import APIRouter

from app.auth.views import views

auth_router = APIRouter()
auth_router.include_router(views.router, prefix="")
