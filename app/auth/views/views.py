from typing import Union
from fastapi import APIRouter

router = APIRouter()

@router.post("/signup", name="Signup")
def signup():
    """
    Signs up a new user.

    Returns:
        str: Message indicating successful user signup.
    """
    return "Signup User"

@router.post("/login", name="Login")
def login():
    """
    Logs in a user.

    Returns:
        str: Message indicating successful user login.
    """
    return "Login User"

@router.post("/logout/{user_id}", name="Logout")
def logout(user_id: int):
    """
    Logs out a user.

    Args:
        user_id (int): ID of the user.

    Returns:
        str: Message indicating successful user logout.
    """
    return "Logout"
