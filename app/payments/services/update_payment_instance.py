def update_payment(payment_id, provider=None, customer_id=None, plan_id=None, plan_units=None):



    if payment is None:
        session.close()
        return  # Or raise an appropriate exception

    if provider is not None:
        payment.provider = provider
    if customer_id is not None:
        payment.provider_customer_id = customer_id
    if plan_id is not None:
        payment.provider_plan_id = plan_id
    if plan_units is not None:
        payment.provider_plan_units = plan_units

    session.commit()
    session.close()