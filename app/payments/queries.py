from app.api.config.database import get_db
from app.models.user import User
from app.models.payment import Payment
from app.models.transactions import Transaction

def get_all_transactions_by_user_id_query(user_id):
    db = next(get_db())
    query = db.select(Transaction).where(Transaction.user_id == user_id)
    return db.execute(query).fetchall()


def get_transaction_instance(payment_instance_id):
    db = next(get_db())
    query = db.select(Transaction).where(Transaction.id == payment_instance_id)
    return db.execute(query).first()


def get_payment_instance(user_id):
    db = next(get_db())
    query = db.select(Payment).where(Payment.user_id == user_id)
    return db.execute(query).first()


