from pydantic import BaseModel


class StatementItem(BaseModel):
    time: int
    description: str
    mcc: int
    amount: int
    operationAmount: int
    currencyCode: int
    commissionRate: int
    receiptId: str


class MonoWebHookData(BaseModel):
    account: str
    statementItem: StatementItem


class MonoWebHookBody(BaseModel):
    type: str
    data: MonoWebHookData
