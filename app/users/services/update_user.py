from app.users.queries import get_user_by_query, update_user_query


def update_user_svc(user_id, data):
    try:
        update_user_query(user_id, data)
        return True
    except:
        return False


