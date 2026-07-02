from helpers import set_default_layout

def create_accounts_sheet(workbook, styles):
    ws = workbook.add_worksheet("Accounts")

    set_default_layout(ws)

    ws.set_column("A:H", 20)

    ws.merge_range(
        "A1:H2",
        "Accounts",
        styles["title"]
    )

    headers = [
        "Account ID",
        "Account Name",
        "Type",
        "Bank",
        "Opening Balance",
        "Current Balance",
        "Currency",
        "Active"
    ]

    for col, header in enumerate(headers):
        ws.write(3, col, header, styles["table_header"])