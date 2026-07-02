from models.account import Account


class AccountService:

    def __init__(self):
        self._accounts: list[Account] = []

    def add(self, account: Account) -> None:
        self._accounts.append(account)

    def all(self) -> list[Account]:
        return self._accounts

    def active(self) -> list[Account]:
        return [a for a in self._accounts if a.active]