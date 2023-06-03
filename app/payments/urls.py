from fastapi import APIRouter

from app.payments.views import views

payment_router = APIRouter()
payment_router.include_router(views.router,prefix="")
