from typing import Union
from fastapi import APIRouter

router = APIRouter()

@router.get("/{user_id}/history", name="Payments History")
def payments_history(user_id: int):
    """
    Retrieves the payment history for a user.

    Args:
        user_id (int): ID of the user.

    Returns:
        str: Message indicating successful retrieval of payment history.
    """
    return "Payments History"


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
    return "Payments Refund"


@router.get("/{user_id}/create_checkout_session", name="Create Checkout Session")
def create_checkout_session(user_id: int):
    """
    Creates a checkout session for a user.

    Args:
        user_id (int): ID of the user.

    Returns:
        str: Message indicating successful creation of a checkout session.
    """
    return "Create Checkout Session"


@router.get("/{user_id}/customer_portal_session", name="Customer Portal Session")
def customer_portal_session(user_id: int):
    """
    Retrieves the customer portal session for a user.

    Args:
        user_id (int): ID of the user.

    Returns:
        str: Message indicating successful retrieval of the customer portal session.
    """
    return "Customer Portal Session"
