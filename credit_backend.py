#!/usr/bin/env python3 -u

import argparse

from db_handler import db_handler
from excel_handler import get_data_from_excel


def parse_args():
    parser = argparse.ArgumentParser(prog="Credit Display", usage="Display credit expanses")
    parser.add_argument('--sheet_name', help='Original excel file from credit card company',
                        default="credit_expenses.xls", required=True)
    parser.add_argument('--db_user', help='User name to connect to database',
                        required=True)
    parser.add_argument('--db_pass', help='Password to connect to database',
                        required=True)
    parser.add_argument('--db_name', help='Database name', required=True)
    parser.add_argument('--collection', help='Collection name', required=True)

    return parser.parse_args()


def function_caller(choice):
    return {
        'i': 'insert_transactions',
        'rmc': 'remove_collection_from_db',
        'gsa': 'get_shop_and_amount',
        'gcl': 'get_collections_list',
        'usg': 'update_shop_group',
        'q': 'exit'
    }.get(choice, None)


def get_parameters(function_name):
    return {
        'insert_transactions': 'transactions_arr',
        'remove_collection_from_db': 'col',
        'get_shop_and_amount': '',
        'get_collections_list': '',
        'usg': 'get_input_shop_group',
        'q': '0'
    }.get(function_name, None)


def help_print():
    print("Welcome to Credit Display!\nPlease choose what to do:")
    print("'i' - Inserts transactions from excel to current collection\n"
          "'gsa' - Print shop and amount\n"
          "'rmc' - Remove current collection\n"
          "'gcl' - Get a list of all collections in DB\n"
          "'usg' - Update the shop group collection\n"
          "'q' - Exit the program")


def main():
    args = parse_args()
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
            if func == 'exit':
                exit(0)
            if func == 'update_shop_group':
                shop = input("Please enter the shop name\n")
                group = input("Please enter the group name\n")
                getattr(db, func)(shop, group)
                break
            if arg:
                ans = getattr(db, func)(eval(arg))
            else:
                ans = getattr(db, func)()

            print("Function {0} parameters: {1}, Returned:\n{2}".format(func, arg, ans))
        else:
            print("Function not found!")


if __name__ == "__main__":
    main()
