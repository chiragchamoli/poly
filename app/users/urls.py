from fastapi import APIRouter

from app.users.views import views

user_router = APIRouter()
user_router.include_router(views.router,  prefix="")
