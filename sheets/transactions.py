from helpers import set_default_layout

HEADERS = [
    "Date",
    "Transaction Type",
    "Source",
    "Destination",
    "Category",
    "Amount",
    "Notes",
]


def create_transactions_sheet(workbook, styles):

    ws = workbook.add_worksheet("Transactions")

    set_default_layout(ws)

    ws.set_zoom(110)

    ws.freeze_panes(4, 0)

    ws.set_column("A:A", 15)
    ws.set_column("B:B", 18)
    ws.set_column("C:D", 28)
    ws.set_column("E:E", 24)
    ws.set_column("F:F", 18)
    ws.set_column("G:G", 40)

    ws.merge_range(
        "A1:G2",
        "Transactions",
        styles["title"],
    )

    for col, header in enumerate(HEADERS):
        ws.write(3, col, header, styles["table_header"])

    # Transaction Type dropdown
    ws.data_validation(
        "B5:B5000",
        {
            "validate": "list",
            "source": "=TransactionType",
        },
    )

    # Amount format
    ws.set_column(
        "F:F",
        18,
        styles["money"],
    )