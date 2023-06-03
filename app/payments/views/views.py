from typing import Union
from fastapi import APIRouter, HTTPException

from app.payments.schema import TransactionSchema
from app.payments.services.create_checkout_session import create_customer_checkout_session
from app.payments.services.create_customer_portal_sessions import create_customer_portal_session
from app.payments.services.retrive_transaction import retrieve_transactions
from app.payments.services.start_refund import initiate_payment_refund

router = APIRouter()

@router.get("/{user_id}/history", name="Payments History")
def payments_history(user_id: int):
    """
    Retrieves the payment history for a user.

    Args:
        user_id (int): ID of the user.

    Returns:
        List of all the Transactions
    """
    transaction_instances = retrieve_transactions(user_id)
    serialized_transactions = [
        TransactionSchema(
            id=transaction.id,
            name=transaction.name,
            provider= transaction.provider,
            provider_payment_reference_id = transaction.provider_payment_reference_id,
            payment_status = transaction.payment_status,
            amount = transaction.amount,
            currency = transaction.currency,
            invoice_url = transaction.invoice_url,
        )
        for transaction in transaction_instances
    ]

    return serialized_transactions



@router.get("/{user_id}/refund/{payment_instance_id}", name="Payments Instance Refund")
def payment_refund(user_id: int, payment_instance_id: str):
    """
    Refunds a specific payment instance for a user.

    Args:
        user_id (int): ID of the user.
        payment_instance_id (str): ID of the payment instance.

    Returns:
        str: Message indicating successful refund of a payment instance.
    """
    if initiate_payment_refund(user_id, payment_instance_id):
        return "Refund has been initiated"

    raise HTTPException(status_code=400, detail="Invalid request")


@router.get("/{user_id}/create_checkout_session", name="Create Checkout Session")
def create_checkout_session(user_id: int):
    """
    Creates a checkout session for a user.

    Args:
        user_id (int): ID of the user.

    Returns:
        dict: Message indicating successful creation of a checkout session.
    """

    return create_customer_checkout_session(user_id)


@router.get("/{user_id}/customer_portal_session", name="Customer Portal Session")
def customer_portal_session(user_id: int):
    """
    Retrieves the customer portal session for a user.

    Args:
        user_id (int): ID of the user.

    Returns:
        str: Message indicating successful retrieval of the customer portal session.
    """
    return create_customer_portal_session(user_id)
