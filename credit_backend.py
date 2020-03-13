import argparse
import json
import re
import xlrd

from datetime import datetime
from db_handler import db_handler
from pymongo import MongoClient
from xlrd.sheet import ctype_text


def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--sheet_name', help='Original excel file from credit card company',
                        default="credit_expenses.xls", required=False)
    parser.add_argument('--db_user', help='User name to connect to database',
                        required=True)
    parser.add_argument('--db_pass', help='Password to connect to database',
                        required=True)
    parser.add_argument('--db_name', help='Database name', required=True)
    parser.add_argument('--collection', help='Collection name', required=True)

    return parser.parse_args()


def is_excel_date_type(cell):
    if (cell.ctype == 3):
        return True
    return False


def excel_date_to_datetime(cell, workbook):
    py_date = datetime(
        *xlrd.xldate_as_tuple(cell.value, workbook.datemode))
    # TODO : caclcaute generel year,now only for 2020 s.t = 2020/100 = 20
    date = "{}/{}/{}".format(py_date.day, py_date.month, int(py_date.year / 100))
    return str(date)


def get_transactions(workbook, first_sheet, type):
    transactions = list()
    for i in range(first_sheet.nrows):
        row = first_sheet.row(i)
        # unpack row to vars ,str each element for json
        data = [str(element).replace("text", '') for element in row]
        if type == "isracard":
            [date, bussiness_name, deal_value, currency1, charge_value, currency2, voucher_number, more_details] = data
            deal_value += " " + currency1
            charge_value += " " + currency2
        else:
            [date, bussiness_name, deal_value, charge_value, more_details] = data
            if (is_excel_date_type(row[0])):
                date = (excel_date_to_datetime(row[0], workbook))
        clean_date = re.sub(r'[^-//0-9]', "", date)
        curr_deal = {'deal_date ': clean_date, 'bussiness_name': (bussiness_name), 'deal_value': (deal_value),
                     'charge_value': (charge_value),
                     'more_details': (more_details)}
        print(curr_deal)
        transactions.append(curr_deal)
    return transactions


def get_data_from_excel(sheet_name, type="default"):
    """Gets all transaction from supplied excel sheet"""
    workbook = xlrd.open_workbook(sheet_name)
    first_sheet = workbook.sheet_by_index(0)
    print("First sheet name: '%s'" % first_sheet.name)

    return get_transactions(workbook, first_sheet, type)


def main():
    args = parse_args()
    transactions_arr = get_data_from_excel(args.sheet_name)

    print("All tansactions: {0}".format(transactions_arr))
    db = db_handler("mongodb+srv://{0}:{1}@creditdata-xurnm.mongodb.net/test".format(args.db_user, args.db_pass))
    db.connect_to_db(args.db_name)
    if args.collection in db.get_collections_list():
        print("Collection already in db, deleting it...")
        db.remove_collection_from_db(args.collection)
    db.connect_to_collection(args.collection)
    db.insert_transactions(transactions_arr)
    shop_amount = db.get_shop_and_amount()

    print("Shop and amount: {0}".format(shop_amount))


if __name__ == "__main__":
    main()
