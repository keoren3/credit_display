import io
import xlrd

from xlwt import Workbook


def validate_date(xl_date, date_mode):
    updated_date = xl_date.value
    if xl_date.ctype == 3:
        year, day, month = xlrd.xldate_as_tuple(xl_date.value, date_mode)[:-3]
        updated_date = "{0}/{1}/{2}".format(day, month, year)
    elif len(updated_date.split('/')[2]) == 2:
        wrong_year = updated_date.split('/')[2]
        correct_year = '20' + wrong_year
        updated_date = '/'.join(updated_date.split('/')[:-1]) + '/' + correct_year
    return updated_date


def get_data_from_row(row, sheet_type, date_mode):
    print("Checking if a transaction was made in the row: '{0}'".format(row))
    if '.' in str(row[2].value):
        print("A transaction was made! adding it to the database!")
        date = validate_date(row[0], date_mode)
        if sheet_type == 'visa':
            business_name, deal_value, charge_value, more_details = [cell.value for cell in row[1:]]
        if sheet_type == 'mastercard':
            business_name, deal_value, _, charge_value, _, more_details = [cell.value for cell in row[1:-1]]

    return {'deal_date': date, 'business_name': business_name, 'deal_value': deal_value,
            'charge_value': charge_value, 'more_details': more_details}


def get_transactions(work_sheet, sheet_type, date_mode):
    transactions = []
    print("Going over all rows in sheet")

    for i in range(work_sheet.nrows):
        row = work_sheet.row(i)
        curr_deal = get_data_from_row(row, sheet_type, date_mode)
        validate_date(curr_deal['deal_date'])

        if curr_deal:
            print("Adding deal '{0}' to transactions".format(curr_deal))
            transactions.append(curr_deal)

    print("Returning transactions: {0}".format(transactions))
    return transactions


def get_sheet_type(work_sheet):
    if 'ויזה' in work_sheet.row(1)[0].value:
        return 'visa'
    if 'מסטרקארד' in work_sheet.row(3)[0].value:
        return 'mastercard'
    raise KeyError("ERROR: Work sheet {0} is not recognized!".format(work_sheet))


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
    sheet_type = get_sheet_type(work_sheet)
    print("First sheet name: '%s'" % work_sheet.name)

    return get_transactions(work_sheet, sheet_type, workbook.datemode)
