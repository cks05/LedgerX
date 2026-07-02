from dataclasses import dataclass


@dataclass(slots=True)
class Account:
    """
    Represents a financial account.
    """

    account_id: str
    name: str
    account_type: str
    institution: str

    opening_balance: float = 0.0
    current_balance: float = 0.0

    currency: str = "INR"

    active: bool = True