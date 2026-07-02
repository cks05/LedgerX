from dataclasses import dataclass


@dataclass
class Category:
    category_id: int
    category_type: str
    name: str
    color: str
    icon: str
    active: bool = True