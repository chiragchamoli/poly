from pydantic import BaseModel

class TransactionSchema(BaseModel):
    user_id: int
    provider: str
    provider_customer_id: str
    provider_payment_reference_id: str
    payment_status: str
    amount: int
    currency: str
    invoice_url: str