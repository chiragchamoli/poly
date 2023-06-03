from app.api.config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    provider = Column(String)
    provider_customer_id = Column(String)
    provider_payment_reference_id = Column(String)
    # "Paid," "Pending," "Failed," or "Refunded."
    payment_status = Column(String)
    amount = Column(Integer)
    currency = Column(String)
    invoice_url = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

