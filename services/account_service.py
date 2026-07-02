from models.account import Account


class AccountService:
    """Handles account-related operations."""

    def __init__(self):
        self.accounts = []

    def add_account(self, account: Account):
        self.accounts.append(account)

    def get_accounts(self):
        return self.accounts

    def get_active_accounts(self):
        return [a for a in self.accounts if a.active]

    def get_account_by_id(self, account_id: int):
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None