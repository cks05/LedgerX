from helpers import set_default_layout


def create_dashboard_sheet(workbook, styles):

    ws = workbook.add_worksheet("Dashboard")

    set_default_layout(ws)

    ws.set_zoom(110)
    ws.hide_gridlines(2)

    ws.set_column("A:A", 30)
    ws.set_column("B:B", 20)

    # Title
    ws.merge_range(
        "A1:B2",
        "LedgerX Dashboard",
        styles["title"],
    )

    # KPI Labels
    ws.write("A4", "Total Income", styles["table_header"])
    ws.write("A5", "Total Expenses", styles["table_header"])
    ws.write("A6", "Total Savings", styles["table_header"])
    ws.write("A7", "Total Transactions", styles["table_header"])

    # KPI Values (placeholder for now)
    ws.write_number("B4", 0, styles["money"])
    ws.write_number("B5", 0, styles["money"])
    ws.write_number("B6", 0, styles["money"])
    ws.write_number("B7", 0)

    # Monthly Summary
    ws.merge_range(
        "A10:B10",
        "Monthly Summary",
        styles["table_header"],
    )

    # Recent Transactions
    ws.merge_range(
        "A16:B16",
        "Recent Transactions",
        styles["table_header"],
    )