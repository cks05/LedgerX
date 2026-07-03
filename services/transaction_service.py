from models.transaction import Transaction


class TransactionService:
    """
    Handles transaction operations.
    """

    def __init__(self):
        self._transactions: list[Transaction] = []

    def add(self, transaction: Transaction) -> None:
        self._transactions.append(transaction)

    def all(self) -> list[Transaction]:
        return self._transactions

    def count(self) -> int:
        return len(self._transactions)