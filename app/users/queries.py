from sqlalchemy import delete

from app.api.config.database import get_db
from app.models.user import User
from app.models.users_groups import UserGroup
from app.models.group import Group
def create_user_query(user: User):
    db = next(get_db())
    db.add(user)
    db.commit()

def delete_user_query(user_id):
    db = next(get_db())
    query = delete(User).where(User.id == user_id)
    db.execute(query)
    db.commit()


def does_email_exists(email:str):
    db = next(get_db())
    return db.query(User).filter(User.email == email).first()


def update_user_query(user_id, user_data):
    """Update a user instance with the given ID.

    Args:
        user_id: The ID of the user to update.
        user_data: A dictionary of key-value pairs representing the new user data.
    """
    db = next(get_db())
    query = db.update(User).where(User.id == user_id)
    for key, value in user_data.items():
        query = query.set(key, value)
    db.execute(query)
    db.commit()


def get_user_by_query(query_el) -> User:
    """Get a user by ID or email.

    Args:
        session: A SQLAlchemy session object.
        user_id_or_email: The user ID or email of the user to get.

    Returns:
        A user object, or None if the user is not found.
    """
    db = next(get_db())
    query = db.select(User).where(
        (User.id == query_el) | (User.email == query_el)
    )
    return db.execute(query).first()

def get_user_groups(user_id):
    groups_ids = get_groups_for_user(user_id)
    group_instances = get_groups_on_selected_instances(groups_ids)
    return group_instances



def get_groups_for_user(user_id):
    """Get all the groups which a user is part of.

    Args:
        user_id: The ID of the user to get the groups for.
    Returns:
        A list of group ids.
    """
    db = next(get_db())
    query = db.select(UserGroup.group_id).where(UserGroup.id == user_id)
    groups = db.execute(query).fetchall()
    return [group[0] for group in groups]

def get_groups_on_selected_instances(instance_ids):
    """Get all the groups on the selected instances.
    Returns:
        A list of group names.
    """
    db = next(get_db())
    query = db.select(Group.id).where(Group.id in instance_ids)
    groups = db.execute(query).fetchall()
    return [group[0] for group in groups]