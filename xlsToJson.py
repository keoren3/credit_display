import xlrd 
from xlrd.sheet import ctype_text 
from datetime import datetime
import json

def main():
	print("start working on the project")
	convertToJson("new_one.xls")


def isXldateType(cell):
	if(cell.ctype == 3):
		return True
	return False

def changeXldateToDatatime(cell,workbook):
	return xlrd.xldate.xldate_as_datetime(cell.value, workbook.datemode)

def convertToJson(filename):
	curr_workbook = xlrd.open_workbook(filename)

	sheet_names = curr_workbook.sheet_names()

	first_sheet = curr_workbook.sheet_by_name(sheet_names[0])

	first_sheet = curr_workbook.sheet_by_index(0)
	print ('Sheet name: %s' % first_sheet.name)

	with open('jsonFromXls.txt','w') as json_file:
		deals = []
		for i in range(first_sheet.nrows):
			row = first_sheet.row(i)
			#unpack row to vars ,str each element for json 
			[date,bussines_name,deal_value,chrage_value,another_deatils] = [str(element).replace("text",'') for element in row]
			if(isXldateType(row[0])):
				date = str(changeXldateToDatatime(row[0], curr_workbook))
			curr_deal = {'deal_date ' : date ,'bussines_name' : (bussines_name)  ,'deal_value' : (deal_value),'chrage_value' : (chrage_value),
			'more deatils' : (another_deatils)}
			deals.append(curr_deal)
		#ensure ascii = False for current hebrew output
		json.dump(deals,json_file,ensure_ascii = False,indent = 4)
	json_file.close()













if __name__ == "__main__":
	main()