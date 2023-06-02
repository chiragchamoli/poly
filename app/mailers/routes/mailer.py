from fastapi import APIRouter

from app.mailers.views import mailer

router = APIRouter()

router.include_router(mailer.router, tags=["Mailer"], prefix="/send-email")
