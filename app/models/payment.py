from app.api.config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func


class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    provider = Column(String)
    provider_customer_id = Column(String)
    provider_plan_id = Column(String)
    provider_plan_units = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

