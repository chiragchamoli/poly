from app.group.queries import create_group_instance_query
from app.models.group import Group
def create_group_service(data):
    name = data.get("name")
    group = Group(
        name = name
    )
    try:
        create_group_instance_query(group)
        return True
    except Exception:
        return False
