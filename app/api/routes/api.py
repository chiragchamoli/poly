from fastapi import APIRouter

from app.mailers.routes import mailer

router = APIRouter()

router.include_router(mailer.router, tags=["Mailer"], prefix="/mailer")
