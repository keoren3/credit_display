import io
import re
import xlrd

from datetime import datetime
from xlwt import Workbook


def is_excel_date_type(cell):
    if cell.ctype == 3:
        return True
    return False


def excel_date_to_datetime(cell, workbook):
    py_date = datetime(
        *xlrd.xldate_as_tuple(cell.value, workbook.datemode))
    # TODO : calculate general year,now only for 2020 s.t = 2020/100 = 20
    date = "{0}/{1}/{2}".format(py_date.day, py_date.month, int(py_date.year/100))
    return str(date)


def get_transactions(workbook, first_sheet):
    transactions = list()
    for i in range(first_sheet.nrows):
        row = first_sheet.row(i)
        # unpack row to vars ,str each element for json
        [date, business_name, deal_value, charge_value, more_details] = [
            str(element).replace("text", '') for element in row]
        if is_excel_date_type(row[0]):
            date = (excel_date_to_datetime(row[0], workbook))
        clean_date = re.sub(r'[^-//0-9]', "", date)
        curr_deal = {'deal_date': clean_date, 'business_name': business_name, 'deal_value': deal_value, 'charge_value': charge_value,
                     'more_details': more_details}
        print(curr_deal)
        transactions.append(curr_deal)
    return transactions


def fix_corrupt_excel(sheet_name):
    print("Re-creating excel sheet to fix corruption")
    sheet_file = io.open(sheet_name, "r", encoding="utf-16")
    sheet_data = sheet_file.readlines()
    excel_doc = Workbook()
    sheet = excel_doc.add_sheet("FixedSheet", cell_overwrite_ok=True)

    for i, row in enumerate(sheet_data):
        for j, val in enumerate(row.replace('\n', '').split('\t')):
            sheet.write(i, j, val)

    excel_doc.save(sheet_name)
    print("Corruption fixed! Continuing...")


def get_data_from_excel(sheet_name):
    """Gets all transaction from supplied excel sheet"""
    try:
        workbook = xlrd.open_workbook(sheet_name)
    except xlrd.XLRDError as e:
        print("### WARNING: Excel file {0} was corrupted. Exception: '{1}'.".format(sheet_name, e))
        fix_corrupt_excel(sheet_name)
        workbook = xlrd.open_workbook(sheet_name)
    first_sheet = workbook.sheet_by_index(0)
    print("First sheet name: '%s'" % first_sheet.name)

    return get_transactions(workbook, first_sheet)