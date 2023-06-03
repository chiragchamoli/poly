from typing import Union

from bcrypt import checkpw
from fastapi import APIRouter, HTTPException

from app.group.queries import add_user_to_group, remove_user_from_group
from app.group.services.create_group import create_group_service

router = APIRouter()

@router.post("/", name="Create Group")
def create_group(data: dict):
    """
        Create New Group

    Args:
        data (dict): The user data. Expected keys: "name"
    :param data:
    :return:
    """
    group_created = create_group_service(data)

    if group_created:
        return "Group Created"

    raise HTTPException(status_code=400, detail="Invalid request")


@router.post("{group_id}/add-user/{user_id}", name="Create Group")
def add_user_group(user_id:int, group_id:int):
    try:
        add_user_to_group(user_id,group_id)
        return "user added to Group."
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid request")


@router.post("{group_id}/remove-user/{user_id}", name="Create Group")
def add_user_group(user_id:int, group_id:int):
    try:
        remove_user_from_group(user_id, group_id)
        return "user added to Group."
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid request")
