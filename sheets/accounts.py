from helpers import set_default_layout


HEADERS = [
    "Account ID",
    "Account Name",
    "Type",
    "Institution",
    "Opening Balance",
    "Current Balance",
    "Currency",
    "Active",
]


def create_accounts_sheet(workbook, styles):

    ws = workbook.add_worksheet("Accounts")

    set_default_layout(ws)

    ws.set_zoom(110)

    ws.set_column("A:A", 16)
    ws.set_column("B:B", 30)
    ws.set_column("C:C", 18)
    ws.set_column("D:D", 22)
    ws.set_column("E:F", 18)
    ws.set_column("G:G", 12)
    ws.set_column("H:H", 10)

    ws.merge_range(
        "A1:H2",
        "Accounts",
        styles["title"],
    )

    for col, header in enumerate(HEADERS):
        ws.write(3, col, header, styles["table_header"])