import stripe

class StripeHelper:
    def __init__(self, api_key):
        stripe.api_key = api_key

    def create_customer(self, email):
        customer = stripe.Customer.create(email=email)
        return customer.id

    def initiate_refund(self, charge_id):
        refund = stripe.Refund.create(charge=charge_id)
        return refund

    def create_checkout_session(self, customer_id):
        session = stripe.checkout.Session.create(
            customer=customer_id,
            payment_method_types=['card'],
            line_items=[
                {
                    'price': 'price_123',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
        return session.id

    def create_customer_portal(self, customer_id):
        portal = stripe.billing_portal.Session.create(customer=customer_id)
        return portal.url
