from fastapi import APIRouter
from app.payments.urls import payment_router
from app.auth.urls import auth_router
from app.users.urls import user_router
router = APIRouter()

router.include_router(payment_router, tags=["Payments"], prefix="/payments")
router.include_router(auth_router, tags=["Auth"], prefix="/auth")
router.include_router(user_router, tags=["Users"], prefix="/users")


