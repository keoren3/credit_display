#!/usr/bin/env python3 -u

import argparse
import re
import xlrd

from datetime import datetime
from db_handler import db_handler


def parse_args():
    parser = argparse.ArgumentParser(prog="Credit Display", usage="Display credit expanses")
    parser.add_argument('--sheet_name', help='Original excel file from credit card company',
                        default="credit_expenses.xls", required=False)
    parser.add_argument('--db_user', help='User name to connect to database',
                        required=False)
    parser.add_argument('--db_pass', help='Password to connect to database',
                        required=False)
    parser.add_argument('--db_name', help='Database name', required=False)
    parser.add_argument('--collection', help='Collection name', required=False)

    return parser.parse_args()


def function_caller(choice):
    return {
        'i': 'insert_transactions',
        'rmc': 'remove_collection_from_db',
        'gsa': 'get_shop_and_amount',
        'gcl': 'get_collections_list'
    }.get(choice, None)


def get_parameters(function_name):
    return {
        'insert_transactions': 'transactions_arr',
        'remove_collection_from_db': 'col',
        'get_shop_and_amount': '',
        'get_collections_list': ''
    }.get(function_name, None)


def is_excel_date_type(cell):
    if cell.ctype == 3:
        return True
    return False


def excel_date_to_datetime(cell, workbook):
    py_date = datetime(
        *xlrd.xldate_as_tuple(cell.value, workbook.datemode))
    # TODO : calculate general year,now only for 2020 s.t = 2020/100 = 20
    date = "{}/{}/{}".format(py_date.day, py_date.month, int(py_date.year/100))
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
        curr_deal = {'deal_date ': clean_date, 'business_name': business_name, 'deal_value': deal_value, 'charge_value': charge_value,
                     'more_details': more_details}
        print(curr_deal)
        transactions.append(curr_deal)
    return transactions


def get_data_from_excel(sheet_name):
    """Gets all transaction from supplied excel sheet"""
    workbook = xlrd.open_workbook(sheet_name)
    first_sheet = workbook.sheet_by_index(0)
    print("First sheet name: '%s'" % first_sheet.name)

    return get_transactions(workbook, first_sheet)


def help_print():
    print("Welcome to Credit Display!\nPlease choose what to do:")
    print("'i' - Inserts transactions from excel to current collection\n'gsa' - Print shop and amount\n"
          "'rmc' - Remove current collection\n'gcl' - Get a list of all collections in DB")


def main():
    args = parse_args()
    if 'collection' in args:
        col = args.collection
    db = db_handler("mongodb+srv://{0}:{1}@creditdata-xurnm.mongodb.net/test".format(args.db_user, args.db_pass))
    db.connect_to_db(args.db_name)
    db.connect_to_collection(args.collection)
    transactions_arr = get_data_from_excel(args.sheet_name)

    while True:
        help_print()
        choice = input("Please enter you choice:\n")
        func = function_caller(choice)
        arg = get_parameters(func)
        if func:
            if arg:
                ans = getattr(db, func)(eval(arg))
            else:
                ans = getattr(db, func)()

            print("Function {0} parameters: {1}, Returned:\n{2}".format(func, arg, ans))
        else:
            print("Function not found!")


if __name__ == "__main__":
    main()
