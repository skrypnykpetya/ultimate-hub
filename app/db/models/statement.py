from sqlalchemy import Column, Integer, String
from .base import AbstractModel


class Statement(AbstractModel):
    __tablename__ = "statements"
    id = Column(Integer, primary_key=True)
    description = Column(String(250), index=True)
    mcc = Column(Integer, index=True)
    amount = Column(Integer)
    operationAmount = Column(Integer)
    currencyCode = Column(Integer)
    commissionRate = Column(Integer)
    receiptId = Column(String(250))
    time = Column(Integer)
