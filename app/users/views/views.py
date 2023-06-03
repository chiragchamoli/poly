from typing import Union
from fastapi import APIRouter

router = APIRouter()

@router.post("/", name="create user")
def create_user():
    """
    Creates a new user.

    Returns:
        str: Message indicating the successful creation of a user.
    """
    return "Create User"

@router.get("/", name="retrieve user")
def get_user(user_email: Union[str, None] = None, user_id: Union[int, None] = None):
    """
    Retrieves a user by either email or ID.

    Args:
        user_email (str, optional): Email of the user. Defaults to None.
        user_id (int, optional): ID of the user. Defaults to None.

    Returns:
        str: Message indicating the retrieval of a user.
    """
    return "Get user by either email or ID"

@router.get("/{user_id}/groups", name="retrieve all groups for user")
def get_user_groups(user_id: str):
    """
    Retrieves all groups for a user.

    Args:
        user_id (str): ID of the user.

    Returns:
        str: Message indicating the retrieval of user groups.
    """
    return "Get user"

@router.delete("/{user_id}", name="delete user")
def delete_user(user_id: str):
    """
    Deletes a user.

    Args:
        user_id (str): ID of the user.

    Returns:
        str: Message indicating the successful deletion of a user.
    """
    return 'Delete user'

@router.put("/{user_id}", name="update user")
def update_user(user_id: str):
    """
    Updates a user.

    Args:
        user_id (str): ID of the user.

    Returns:
        str: Message indicating the successful update of a user.
    """
    return "Update user"
