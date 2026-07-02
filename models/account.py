from dataclasses import dataclass


@dataclass(slots=True)
class Account:
    """
    Represents a financial account in LedgerX.
    """

    account_id: str
    name: str
    account_type: str
    opening_balance: float = 0.0
    notes: str = ""