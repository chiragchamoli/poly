from app.users.queries import get_user_by_query


def get_user_by(input):

    try:
        return get_user_by_query(input)
    except Exception:
        return None