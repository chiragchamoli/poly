from app.payments.queries import get_transaction_instance
from app.payments.services.stripe import StripeHelper


def initiate_payment_refund(user_id, payment_instance_id):
    try:
        stripe_instance = StripeHelper('stripe_api_key')
        tx_instance = get_transaction_instance(payment_instance_id)
        refund = stripe_instance.initiate_refund(tx_instance.provider_payment_reference_id)
        # ideally we store this
        print('Refund ID:', refund.id)
        return True
    except Exception:
        return False

