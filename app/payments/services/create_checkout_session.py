from app.payments.queries import get_payment_instance
from app.payments.services.stripe import StripeHelper


def create_customer_checkout_session(user_id):
    stripe_instance = StripeHelper('stripe_api_key')
    customer = get_payment_instance(user_id)
    return stripe_instance.create_checkout_session(customer.provider_customer_id)
