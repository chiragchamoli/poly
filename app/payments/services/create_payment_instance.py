from app.models.payment import Payment
from app.payments.queries import create_payment_instance_query
from app.payments.services.stripe import StripeHelper


def create_payment(user_id, user_email, provider, plan_id, plan_units):
    stripe_instance = StripeHelper('stripe_api_key')
    customer_id = stripe_instance.create_customer(user_email)

    payment = Payment(user_id=user_id,
                      provider=provider,
                      provider_customer_id=customer_id,
                      provider_plan_id=plan_id,
                      provider_plan_units=plan_units)


    create_payment_instance_query(payment)
    return True
