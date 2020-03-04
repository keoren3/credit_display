import argparse
import json
import xlrd
import re
from datetime import datetime
from db_handler import db_handler
from pymongo import MongoClient
from xlrd.sheet import ctype_text


def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--sheet_name', help='Original excel file from credit card company',
                        default="credit_expenses.xls", required=False)
    parser.add_argument('--db_user', help='User name to connect to database',
                        default="imridb", required=False)
    parser.add_argument('--db_pass', help='password to connect to database',
                        default="imri123!", required=False)

    return parser.parse_args()


def is_excel_date_type(cell):
    if(cell.ctype == 3):
        return True
    return False


def excel_date_to_datetime(cell, workbook):
    py_date = datetime(
        *xlrd.xldate_as_tuple(cell.value, workbook.datemode))
    # TODO : caclcaute generel year,now only for 2020 s.t = 2020/100 = 20
    date = "{}/{}/{}".format(py_date.day, py_date.month, int(py_date.year/100))
    return str(date)


def get_transactions(workbook, first_sheet):
    transactions = list()
    for i in range(first_sheet.nrows):
        row = first_sheet.row(i)
        # unpack row to vars ,str each element for json
        [date, bussines_name, deal_value, chrage_value, another_details] = [
            str(element).replace("text", '') for element in row]
        if(is_excel_date_type(row[0])):
            date = (excel_date_to_datetime(row[0], workbook))
        clean_date = re.sub(r'[^-//0-9]', "", date)
        curr_deal = {'deal_date ': clean_date, 'bussines_name': (bussines_name), 'deal_value': (deal_value), 'chrage_value': (chrage_value),
                     'more details': (another_details)}
        print(curr_deal)
        transactions.append(curr_deal)
    return transactions


def get_data_from_excel(sheet_name):
    """Gets all transaction from supplied excel sheet"""
    workbook = xlrd.open_workbook(sheet_name)
    first_sheet = workbook.sheet_by_index(0)
    print("First sheet name: '%s'" % first_sheet.name)

    return get_transactions(workbook, first_sheet)


def handle_db(url, collection, data):
    db = db_handler(url, collection)
    db.connect_to_db()
    db.insert_transactions_db(data)


def main():
    args = parse_args()
    transactions_arr = get_data_from_excel(args.sheet_name)

    print("All tansactions: {0}".format(transactions_arr))

    handle_db("mongodb+srv://{0}:{1}@creditdata-xurnm.mongodb.net/test".format(args.db_user, args.db_pass),
              "test-collection", transactions_arr)


if __name__ == "__main__":
    main()
