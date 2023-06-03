from app.users.queries import delete_user_query
def delete_user_svc(user_id):
    try:
        delete_user_query(user_id)
        return True
    except:
        return False



