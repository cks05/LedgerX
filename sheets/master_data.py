from styles import get_styles
from datetime import datetime


def create_dropdown_sheet(workbook, styles):
    """
    Creates the Dropdown Data worksheet.
    This sheet stores values used in data validation lists.
    """
    ws = workbook.add_worksheet("Dropdown Data")
    ws.hide_gridlines(2)

    # -----------------------------
    # Column Widths
    # -----------------------------
    ws.set_column("A:A", 25)
    ws.set_column("C:C", 25)

    # -----------------------------
    # Title
    # -----------------------------
    ws.merge_range("A1:F2", "Dropdown Data", styles["title"])

    # -----------------------------
    # Headers
    # -----------------------------
    ws.write("A4", "Year Dropdown", styles["section"])
    ws.write("C4", "Period Dropdown", styles["section"])

    # -----------------------------
    # Years
    # -----------------------------
    years = ["Current Year"]

    current_year = datetime.now().year

    for year in range(current_year, current_year + 26):
        years.append(str(year))

    row = 4

    for item in years:
        ws.write(row, 0, item)
        row += 1

    # -----------------------------
    # Periods
    # -----------------------------
    periods = [
        "Total Year",
        "Current Month",
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    row = 4

    for item in periods:
        ws.write(row, 2, item)
        row += 1

    # -----------------------------
    # Named Ranges
    # -----------------------------
    workbook.define_name(
        "YearList",
        "='Dropdown Data'!$A$5:$A$31"
    )

    workbook.define_name(
        "PeriodList",
        "='Dropdown Data'!$C$5:$C$18"
    )