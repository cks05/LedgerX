from helpers import set_default_layout

HEADERS = [
    "Category Type",
    "Parent",
    "Category",
    "Monthly Budget",
    "Notes",
]


def create_categories_sheet(workbook, styles):

    ws = workbook.add_worksheet("Categories")

    set_default_layout(ws)

    ws.set_zoom(110)

    ws.freeze_panes(4, 0)

    ws.set_column("A:A", 18)
    ws.set_column("B:B", 22)
    ws.set_column("C:C", 28)
    ws.set_column("D:D", 18)
    ws.set_column("E:E", 40)

    ws.merge_range(
        "A1:E2",
        "Categories",
        styles["title"],
    )

    for col, header in enumerate(HEADERS):
        ws.write(3, col, header, styles["table_header"])

    # Category Type dropdown
    ws.data_validation(
        "A5:A1000",
        {
            "validate": "list",
            "source": ["Income", "Expense", "Savings"],
        },
    )

    # Currency formatting for Monthly Budget
    ws.set_column(
        "D:D",
        18,
        styles["money"],
    )