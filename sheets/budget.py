from constants import (
    MONTHS,
    INCOME_CATEGORIES,
    EXPENSE_CATEGORIES,
    SAVINGS_CATEGORIES,
)

from helpers import set_default_layout, write_budget_section


def create_budget_planning_sheet(workbook, styles):

    ws = workbook.add_worksheet("Budget Planning")

    set_default_layout(ws)

    ws.set_column("A:A", 28)

    for col in range(1, 13):
        ws.set_column(col, col, 14)

    ws.set_column(13, 13, 16)

    ws.merge_range("A1:N2", "Budget Planning", styles["title"])

    headers = ["Category"] + MONTHS + ["Total"]

    for col, header in enumerate(headers):
        ws.write(3, col, header, styles["table_header"])

    row = 4

    row = write_budget_section(
        ws,
        row,
        "INCOME",
        INCOME_CATEGORIES,
        styles["green"],
        styles["normal"],
        styles["total"],
    )

    row = write_budget_section(
        ws,
        row,
        "EXPENSES",
        EXPENSE_CATEGORIES,
        styles["red"],
        styles["normal"],
        styles["total"],
    )

    row = write_budget_section(
        ws,
        row,
        "SAVINGS",
        SAVINGS_CATEGORIES,
        styles["blue"],
        styles["normal"],
        styles["total"],
    )