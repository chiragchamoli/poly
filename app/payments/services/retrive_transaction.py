from app.payments.queries import get_all_transactions_by_user_id_query


def retrieve_transactions(user_id):
    return get_all_transactions_by_user_id_query(user_id)

