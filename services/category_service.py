from models.category import Category


class CategoryService:
    """
    Handles category operations.
    """

    def __init__(self):
        self._categories: list[Category] = []

    def add(self, category: Category) -> None:
        self._categories.append(category)

    def all(self) -> list[Category]:
        return self._categories

    def by_type(self, category_type: str) -> list[Category]:
        return [
            category
            for category in self._categories
            if category.category_type == category_type
        ]