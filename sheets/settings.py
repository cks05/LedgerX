from datetime import datetime
from helpers import set_default_layout, write_labels

def create_settings_sheet(workbook, styles):
    ws = workbook.add_worksheet("Settings")

    set_default_layout(ws)

    ws.set_column("A:A", 28)
    ws.set_column("B:B", 22)
    ws.set_column("C:C", 18)

    ws.merge_range("A1:C2", "Finance Tracker Settings", styles["title"])
    ws.merge_range("A4:C4", "General Settings", styles["section"])

    labels = [
        "Selected Year",
        "Selected Period",
        "Currency",
        "Savings Goal (%)"
    ]

    write_labels(ws, 4, labels, styles["normal"])

    ws.write("B5", datetime.now().year)
    ws.write("B6", "Current Month")
    ws.write("B7", "INR")
    ws.write("B8", 0.20, styles["percent"])

    ws.data_validation("B5", {"validate": "list", "source": "=YearList"})
    ws.data_validation("B6", {"validate": "list", "source": "=PeriodList"})
    ws.data_validation(
        "B7",
        {"validate": "list", "source": ["INR", "USD", "EUR", "GBP"]},
    )