import xlsxwriter

from services.workbook_builder import WorkbookBuilder


OUTPUT_FILE = r"E:\LedgerX\output\LedgerX.xlsx"


def main():

    workbook = xlsxwriter.Workbook(OUTPUT_FILE)

    builder = WorkbookBuilder(workbook)

    builder.build()

    workbook.close()

    print("LedgerX workbook created successfully.")


if __name__ == "__main__":
    main()