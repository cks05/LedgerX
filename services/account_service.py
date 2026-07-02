from models.account import Account


class AccountService:
    """
    Handles account operations.
    """

    def __init__(self):
        self._accounts: list[Account] = []

    def add(self, account: Account) -> None:
        self._accounts.append(account)

    def all(self) -> list[Account]:
        return self._accounts

    def count(self) -> int:
        return len(self._accounts)