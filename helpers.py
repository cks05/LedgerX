def set_default_layout(ws):
    """Apply the default worksheet layout."""
    ws.hide_gridlines(2)
    ws.freeze_panes(4, 0)


def write_labels(ws, start_row, labels, style):
    """Write a vertical list of labels."""
    row = start_row
    for label in labels:
        ws.write(row, 0, label, style)
        row += 1

def write_budget_section(
    ws,
    start_row,
    title,
    categories,
    title_style,
    cell_style,
    total_style,
):
    """
    Creates a budget section (Income, Expenses, Savings).

    Returns the next available row.
    """

    # Section title
    ws.merge_range(start_row, 0, start_row, 13, title, title_style)
    row = start_row + 1

    for category in categories:
        ws.write(row, 0, category, cell_style)

        # January -> December
        for col in range(1, 13):
            ws.write_blank(row, col, None, cell_style)

        # Total column
        ws.write_formula(
            row,
            13,
            f"=SUM(B{row+1}:M{row+1})",
            total_style,
        )

        row += 1

    # Total row
    ws.write(row, 0, f"TOTAL {title}", title_style)

    for col in range(1, 13):
        col_letter = chr(65 + col)  # B-M
        first = start_row + 2
        last = row
        ws.write_formula(
            row,
            col,
            f"=SUM({col_letter}{first}:{col_letter}{last})",
            total_style,
        )

    ws.write_formula(
        row,
        13,
        f"=SUM(N{start_row+2}:N{row})",
        total_style,
    )

    return row + 2