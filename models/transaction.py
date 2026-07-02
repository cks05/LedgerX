from dataclasses import dataclass
from datetime import date


@dataclass
class Transaction:
    transaction_id: int
    transaction_date: date
    account_id: int
    category_id: int
    amount: float
    description: str
    payee: str