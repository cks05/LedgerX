from dataclasses import dataclass
from datetime import date


@dataclass
class Goal:
    goal_id: int
    name: str
    target_amount: float
    current_amount: float
    target_date: date