from dataclasses import dataclass


@dataclass(slots=True)
class Category:
    """
    Represents a LedgerX category.
    """

    category_type: str
    parent: str
    name: str
    budgetable: bool = True
    notes: str = ""