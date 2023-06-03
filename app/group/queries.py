from app.api.config.database import get_db
from app.models.group import Group
from app.models.users_groups import UserGroup

def create_group_instance_query(group: Group):
    db = next(get_db())
    db.add(group)
    db.commit()


def create_group_group_instance_query(usergroup: UserGroup):
    db = next(get_db())
    db.add(usergroup)
    db.commit()


def add_user_to_group(user_id, group_id):
    # Create a session
    db = next(get_db())
    # Create a new UserGroup instance
    user_group = UserGroup(user_id=user_id, group_id=group_id)
    # Add the user to the group
    db.add(user_group)
    db.commit()
    # Close the session
    db.close()

# Function to remove a user from a group
def remove_user_from_group(user_id, group_id):
    # Create a session
    db = next(get_db())
    user_group = db.query(UserGroup).filter(
        UserGroup.user_id == user_id,
        UserGroup.group_id == group_id
    ).first()
    if user_group:
        db.delete(user_group)
        db.commit()

    # Close the session
    db.close()