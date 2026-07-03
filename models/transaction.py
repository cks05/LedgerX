from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class Transaction:
    """
    Represents a financial transaction in LedgerX.
    """

    transaction_date: date
    transaction_type: str

    source: str
    destination: str

    category: str

    amount: float

    notes: str = ""