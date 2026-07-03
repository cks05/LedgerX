from helpers import (
    set_default_layout,
    create_kpi_card,
    create_section_title,
)

# ----------------------------
# Layout Constants
# ----------------------------

FIRST_CARD_ROW = 3
SECOND_CARD_ROW = 8

COL1 = 0      # A
COL2 = 4      # E
COL3 = 8      # I

CHART_ROW = 13
RECENT_ROW = 30
ALERT_ROW = 45


KPI_CARDS = [
    ("💰 Income", "₹0", FIRST_CARD_ROW, COL1),
    ("💸 Expenses", "₹0", FIRST_CARD_ROW, COL2),
    ("🏦 Savings", "₹0", FIRST_CARD_ROW, COL3),

    ("📈 Cash Flow", "₹0", SECOND_CARD_ROW, COL1),
    ("📊 Net Worth", "₹0", SECOND_CARD_ROW, COL2),
    ("📋 Transactions", "0", SECOND_CARD_ROW, COL3),
]


def create_dashboard_sheet(workbook, styles):
    """
    Creates the Dashboard sheet.
    """

    ws = workbook.add_worksheet("Dashboard")

    set_default_layout(ws)

    ws.set_zoom(110)

    # Dashboard Grid
    for col in range(12):  # A:L
        ws.set_column(col, col, 16)

    # Title
    ws.merge_range(
        "A1:T2",
        "LedgerX Dashboard",
        styles["title"],
    )

    # KPI Cards
    for title, value, row, col in KPI_CARDS:
        create_kpi_card(
            ws,
            title,
            value,
            row,
            col,
            styles,
        )

    # Income vs Expense
    create_section_title(
        ws,
        "A13:F13",
        "📈 Income vs Expense",
        styles,
    )

    create_section_title(
        ws,
        "G13:L13",
        "🥧 Spending by Category",
        styles,
    )

    # Recent Transactions
    create_section_title(
        ws,
        "A30:T30",
        "🕒 Recent Transactions",
        styles,
    )

    # Alerts
    create_section_title(
        ws,
        "A45:T45",
        "⚠ Alerts",
        styles,
    )