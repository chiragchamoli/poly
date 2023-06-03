from typing import Union
from fastapi import APIRouter, HTTPException

from app.users.services.delete_user import delete_user_svc
from app.users.services.fetch_user_groups import get_user_groups_svc
from app.users.services.get_user_by import get_user_by
from app.users.schema import UserResponse
from app.users.services.create_user import create_user_svc
from app.users.services.update_user import update_user_svc
from app.users.services.validation import validate_user_object

router = APIRouter()


@router.post("/", name="create user")
def create_user(data: dict):
    """Creates a new user.

        Args:
            data (dict): The user data.

        Raises:
            HTTPException: If the request is invalid.

        Returns:
            dict: The response data.
        """
    email = data.get("email")
    password = data.get("password")
    fullname = data.get("full_name")
    # validation
    if not validate_user_object(**data):
        raise HTTPException(status_code=400, detail="Invalid request")
    user_created_flag = create_user_svc(email, password, fullname)
    if not user_created_flag:
        raise HTTPException(status_code=400, detail="Invalid request")
    return {"message": "Created"}


@router.get("/", name="retrieve user", response_model=UserResponse)
def get_user(user_email: Union[str, None] = None, user_id: Union[int, None] = None):
    """
    Retrieves a user by either email or ID.

    Args:
        user_email (str, optional): Email of the user. Defaults to None.
        user_id (int, optional): ID of the user. Defaults to None.

    Returns:
        str: Message indicating the retrieval of a user.
    """
    if not user_email and not user_id:
        raise HTTPException(status_code=400, detail="Invalid request")
    input_req = user_email or user_id
    user_instance = get_user_by(input_req)
    if user_instance is None:
        raise HTTPException(status_code=404, detail="Not Found")

    return user_instance.dict()


@router.get("/{user_id}/groups", name="retrieve all groups for user")
def get_user_groups(user_id: int):
    """
    Retrieves all groups for a user.

    Args:
        user_id (str): ID of the user.

    Returns:
        str: Message indicating the retrieval of user groups.
    """
    groups_dict = []
    group_instances = get_user_groups_svc(user_id)
    for gi in group_instances:
        groups_dict.append({
            "id": gi.id,
            "name": gi.name
        })
    return groups_dict


@router.delete("/{user_id}", name="delete user")
def delete_user(user_id: int):
    """
    Deletes a user.

    Args:
        user_id (str): ID of the user.

    Returns:
        str: Message indicating the successful deletion of a user.
    """
    if delete_user_svc(user_id):
        return 'User Deleted'

    raise HTTPException(status_code=404, detail="Not Found")


@router.put("/{user_id}", name="update user")
def update_user(user_id: str, data: dict):
    """
    Updates a user.

    Args:
        user_id (str): ID of the user.

    Returns:
        str: Message indicating the successful update of a user.
    """
    if update_user_svc(user_id, data):
        return 'User Updated'

    raise HTTPException(status_code=404, detail="Not Found")
