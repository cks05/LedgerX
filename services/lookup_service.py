from constants import TRANSACTION_TYPES
from xlsxwriter.utility import xl_col_to_name

class LookupService:

    SHEET_NAME = "_Lookup"

    def __init__(self, workbook):
        self.workbook = workbook
        self.ws = workbook.add_worksheet(self.SHEET_NAME)

        self.ws.hide()

    def write_list(self, column, title, values):
        self.ws.write(0, column, title)

        for row, value in enumerate(values, start=1):
            self.ws.write(row, column, value)

        last_row = len(values) + 1

        column_letter = xl_col_to_name(column)

        self.workbook.define_name(
            title,
            f"='{self.SHEET_NAME}'!${column_letter}$2:${column_letter}${last_row}"
        )

    def create(self):

        self.write_list(
            column=0,
            title="TransactionType",
            values=TRANSACTION_TYPES,
        )