from app.users.queries import get_user_groups


def get_user_groups_svc(input):
    try:
        return get_user_groups(input)
    except Exception:
        return None