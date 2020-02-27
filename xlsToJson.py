import argparse
import json
import xlrd

from datetime import datetime
from db_handler import connect_to_db
from db_handler import insert_db
from pymongo import MongoClient
from xlrd.sheet import ctype_text


def parse_args():
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('--sheet_name', help='sum the integers (default: find the max)', default="new_one.xls", required=False)

	return parser.parse_args()


def isXldateType(cell):
	if(cell.ctype == 3):
		return True
	return False


def changeXldateToDatatime(cell,workbook):
	return xlrd.xldate.xldate_as_datetime(cell.value, workbook.datemode)


def create_data(sheet, curr_workbook):
	transactions = list()
	for i in range(sheet.nrows):
		row = sheet.row(i)
		#unpack row to vars ,str each element for json 
		[date,bussines_name,deal_value,chrage_value,another_deatils] = [str(element).replace("text",'') for element in row]
		if(isXldateType(row[0])):
			date = str(changeXldateToDatatime(row[0], curr_workbook))
		curr_deal = {'deal_date ' : date ,'bussines_name' : (bussines_name)  ,'deal_value' : (deal_value),'chrage_value' : (chrage_value),
		'more deatils' : (another_deatils)}
		transactions.append(curr_deal)
	return transactions


def main():
	args = parse_args()
	curr_workbook = xlrd.open_workbook(args.sheet_name)
	first_sheet = curr_workbook.sheet_by_index(0)
	print ('Sheet name: %s' % first_sheet.name)

	data_arr = create_data(first_sheet, curr_workbook)

	db_con = connect_to_db("mongodb+srv://imridb:imri123!@creditdata-xurnm.mongodb.net/test", "test-collection")
	print("Connected!")
	insert_db(db_con, data_arr)


if __name__ == "__main__":
	main()