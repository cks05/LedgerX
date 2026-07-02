from dataclasses import dataclass


@dataclass
class Budget:
    category_id: int
    month: int
    year: int
    planned_amount: float