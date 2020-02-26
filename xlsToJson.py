import xlrd 
from xlrd.sheet import ctype_text 
from datetime import datetime
import json

def main():
	print("start working on the project")
	convertToJson()


def convertToJson():
	xl_workbook = xlrd.open_workbook("new_one.xls")

# List sheet names, and pull a sheet by name
#
	sheet_names = xl_workbook.sheet_names()
	# print('Sheet Names', sheet_names)

	xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])

# Or grab the first sheet by index 
#  (sheets are zero-indexed)
#
	xl_sheet = xl_workbook.sheet_by_index(0)
	print ('Sheet name: %s' % xl_sheet.name)

	# Pull the first row by index
	#  (rows/columns are also zero-indexed)
	#
	row = xl_sheet.row(0)  # 1st row
	# Print 1st row values and types
	#
	  

	# print('(Column #) type:value')
	# for idx, cell_obj in enumerate(row):
	#     cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
	#     print('(%s) %s %s' % (idx, cell_type_str, cell_obj.value))

	# Print all values, iterating through rows and columns
	#

	with open('jsonFromXls.txt','w') as json_file:
		deals = []
		for i in range(xl_sheet.nrows):
			row = xl_sheet.row(i)
			[date,bussines_name,deal_value,chrage_value,another_deatils] = row
			if(row[0].ctype == 3):
				date = xlrd.xldate.xldate_as_datetime(row[0].value, xl_workbook.datemode)
			else:
				date = row[0]
			curr_deal = {'deal_date ' : str(date).replace("text",'') ,'bussines_name' : str(bussines_name.value)  ,'deal_value' : str(deal_value.value),'chrage_value' : str(chrage_value.value),
			'more deatils' : str(another_deatils.value)}
			deals.append(curr_deal)
		json.dump(deals,json_file,ensure_ascii = False,indent = 4)
			# print(row)
	json_file.close()
	# num_cols = xl_sheet.ncols   # Number of columns
	# for row_idx in range(0, xl_sheet.nrows):    # Iterate through rows
	#     print ('-'*40)
	#     print ('Row: %s' % row_idx)   # Print row number
	#     for col_idx in range(0, num_cols):  # Iterate through columns
	#         cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
	#         # print(cell_obj.value)
	#         if(cell_obj.ctype == 3):
	#         	print ('Column: [%s] cell_obj: [%s]' % (col_idx, xlrd.xldate.xldate_as_datetime(cell_obj.value, xl_workbook.datemode)))
	#         else:	# print(xlrd.xldate.xldate_as_datetime(cell_obj.value, xl_workbook.datemode))
	#         	print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))














if __name__ == "__main__":
	main()