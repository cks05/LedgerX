from config import *

def get_styles(workbook):

    title = workbook.add_format({
        "bold": True,
        "font_size": TITLE_SIZE,
        "font_color": "white",
        "bg_color": PRIMARY,
        "align": "center",
        "valign": "vcenter"
    })

    section = workbook.add_format({
        "bold": True,
        "bg_color": PRIMARY,
        "font_color": "white",
        "border": 1,
        "align": "center"
    })

    header_green = workbook.add_format({
        "bold": True,
        "bg_color": GREEN,
        "font_color": "white",
        "border": 1
    })

    header_red = workbook.add_format({
        "bold": True,
        "bg_color": RED,
        "font_color": "white",
        "border": 1
    })

    header_blue = workbook.add_format({
        "bold": True,
        "bg_color": BLUE,
        "font_color": "white",
        "border": 1
    })

    normal = workbook.add_format({
        "border": 1
    })

    money = workbook.add_format({
        "border": 1,
        "num_format": "₹#,##0.00"
    })

    percent = workbook.add_format({
        "num_format": "0%",
        "border": 1
    })
    table_header = workbook.add_format({
        "bold": True,
        "bg_color": "#D9EAD3",
        "border": 1,
        "align": "center"
    })
    total = workbook.add_format({
        "bold": True,
        "bg_color": "#FFF2CC",
        "border": 1,
        "num_format": "₹#,##0.00"
    })


    return {
        "title": title,
        "section": section,
        "green": header_green,
        "red": header_red,
        "blue": header_blue,
        "normal": normal,
        "money": money,
        "percent": percent,
        "table_header": table_header,
        "total": total,
    }

