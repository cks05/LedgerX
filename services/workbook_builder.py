from sheets.budget import create_budget_planning_sheet
from styles import get_styles
from sheets.settings import create_settings_sheet
from sheets.transactions import create_transactions_sheet
from sheets.categories import create_categories_sheet
from sheets.accounts import create_accounts_sheet
from services.lookup_service import LookupService
from sheets.dashboard import create_dashboard_sheet

class WorkbookBuilder:
    """
    Responsible for creating the LedgerX workbook.
    """

    def __init__(self, workbook):
        self.workbook = workbook
        self.styles = get_styles(workbook)

    def build(self):
        """
        Build all workbook sheets.
        """

        create_settings_sheet(
            self.workbook,
            self.styles,
        )

        create_accounts_sheet(
            self.workbook,
            self.styles,
        )

        create_categories_sheet(
            self.workbook,
            self.styles,
        )

        lookup = LookupService(self.workbook)
        lookup.create()

        create_transactions_sheet(
            self.workbook,
            self.styles,
        )

        create_dashboard_sheet(
            self.workbook,
            self.styles,
        )

        create_budget_planning_sheet(
            self.workbook,
            self.styles,
        )