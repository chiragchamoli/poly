from typing import Union

from bcrypt import checkpw
from fastapi import APIRouter, HTTPException

from app.auth.services.token import create_access_token
from app.users.queries import does_email_exists
from app.users.services.create_user import create_user_svc
from app.users.services.validation import validate_user_object

router = APIRouter()

@router.post("/signup", name="Signup")
def signup(data: dict):
    """
    Signs up a new user.

    Args:
        data (dict): The user data. Expected keys: "email", "password", "full_name".

    Raises:
        HTTPException: If the request is invalid.

    Returns:
        dict: The response data. {"message": "Created"} if user is created successfully.
    """
    email = data.get("email")
    password = data.get("password")
    fullname = data.get("full_name")
    # validation
    if not validate_user_object(**data):
        raise HTTPException(status_code=400, detail="Invalid request")
    if user_created_flag := create_user_svc(email, password, fullname):
        return {"message": "Created"}
    else:
        raise HTTPException(status_code=400, detail="Invalid request")

@router.post("/login", name="Login")
def login(email: str, password: str):
    """
    Logs in a user.

    Args:
        email (str): The user's email.
        password (str): The user's password.

    Raises:
        HTTPException: If the email or password is invalid.

    Returns:
        dict: The response data. {"access_token": "jwt_token", "id": user_id, "email": user_email, "last_login": last_login}
    """
    # Check if the email exists in the database
    user = does_email_exists(email)
    if not user:
        raise HTTPException(status_code=404, detail="Email not found")

    # Verify if the password matches the bcrypt hashed password
    if not checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        raise HTTPException(status_code=401, detail="Invalid password")

    # User is correct.
    token = create_access_token(user.id, user.email)
    return {
        "access_token": token,
        "id": user.id,
        "email": user.email,
        "last_login": str(user.last_login)
    }



@router.post("/logout/{user_id}", name="Logout")
def logout(user_id: int):
    """
    Logs out a user.

    Args:
        user_id (int): ID of the user.

    Returns:
        str: Message indicating successful user logout.
    """
    # we will need to delete the token from either session or redis.

    return "Logout"
