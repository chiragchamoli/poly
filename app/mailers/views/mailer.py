from fastapi import APIRouter

router = APIRouter()


@router.get("", name="users:send-email-to-user")
async def send_mail():
    return {
        "message": "mail sent successfully"
    }
