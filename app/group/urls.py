from fastapi import APIRouter

from app.group.views import views

group_router = APIRouter()
group_router.include_router(views.router,prefix="")
