from dataclasses import dataclass

@dataclass
class Account:
    account_id : int
    name : str
    account_type : str
    bank : str
    currency : str = "INR"
    opening_balace = float = 0.0
    current_balance = flaot = 0.0
    active : bool = True

