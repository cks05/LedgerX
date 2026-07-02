from helpers import set_default_layout

HEADERS = [
    "Account ID",
    "Account Name",
    "Type",
    "Opening Balance",
    "Notes",
]


def create_accounts_sheet(workbook, styles):

    ws = workbook.add_worksheet("Accounts")

    set_default_layout(ws)

    ws.set_zoom(110)

    ws.freeze_panes(4, 0)

    ws.set_column("A:A", 18)
    ws.set_column("B:B", 30)
    ws.set_column("C:C", 18)
    ws.set_column("D:D", 18)
    ws.set_column("E:E", 40)

    ws.merge_range(
        "A1:E2",
        "Accounts",
        styles["title"],
    )

    for col, header in enumerate(HEADERS):
        ws.write(3, col, header, styles["table_header"])