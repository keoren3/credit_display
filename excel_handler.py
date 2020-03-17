import io
import xlrd

from xlwt import Workbook


def get_data_from_row(row):
    print("Checking if a transaction was made in the row: '{0}'".format(row))
    if row[2].value:
        print("A transaction was made! adding it to the database!")
        date, business_name, deal_value, charge_value, more_details = [cell.value for cell in row]

    return {'deal_date': date, 'business_name': business_name, 'deal_value': deal_value,
            'charge_value': charge_value, 'more_details': more_details}


def get_transactions(work_sheet):
    transactions = []
    print("Going over all rows in sheet")

    for i in range(work_sheet.nrows):
        row = work_sheet.row(i)
        curr_deal = get_data_from_row(row)

        print("Adding deal '{0}' to transactions".format(curr_deal))
        transactions.append(curr_deal)

    return transactions


def fix_corrupt_excel(sheet_name):
    print("Re-creating excel sheet to fix corruption")
    sheet_file = io.open(sheet_name, "r", encoding="utf-16")
    sheet_data = sheet_file.readlines()
    excel_doc = Workbook()
    sheet = excel_doc.add_sheet("FixedSheet_{0}".format(sheet_name), cell_overwrite_ok=True)

    for i, row in enumerate(sheet_data):
        for j, val in enumerate(row.replace('\n', '').split('\t')):
            sheet.write(i, j, val)

    excel_doc.save(sheet_name)
    print("Corruption fixed! Continuing...")


def get_data_from_excel(sheet_name):
    """Gets all transaction from supplied excel sheet"""
    try:
        print("Getting transactions from excel sheet: '{0}'".format(sheet_name))
        workbook = xlrd.open_workbook(sheet_name)
    except xlrd.XLRDError as e:
        print("### WARNING: Excel file {0} was corrupted. Exception: '{1}'.".format(sheet_name, e))
        fix_corrupt_excel(sheet_name)
        workbook = xlrd.open_workbook(sheet_name)
    work_sheet = workbook.sheet_by_index(0)
    print("First sheet name: '%s'" % work_sheet.name)

    return get_transactions(work_sheet)
