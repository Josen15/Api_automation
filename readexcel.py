#!/usr/bin/python
# -*- coding: utf-8 -*-

import xlrd
import sys
import traceback
from datetime import datetime
from xlrd import xldate_as_tuple
import requests
import json,io,sys,time

reload(sys)
sys.setdefaultencoding('utf-8')


def getdata(filename):
	rbook = xlrd.open_workbook(filename)
	sheetnames=rbook.sheet_names()
	all_data=[]
	
	for x in sheetnames:
		row_content = []
	
		sheet = rbook.sheet_by_name(x)
		rows = sheet.nrows
		cols = sheet.ncols
		all_content = []
		for i in range(rows):
			row_content = []
			for j in range(cols):
				ctype=sheet.cell(i,j).ctype
				cell=sheet.cell_value(i,j)
				if ctype==2 and cell % 1==0:
					cell = int(cell)
				elif ctype==3:
					date=datetime(*xldate_as_tuple(cell,0))
					cell=date.strftime('%Y/%d/%m %H:%M:%S')
				elif ctype==4:
					cell=True if cell == 1 else False
				row_content.append(cell)
				
			all_content.append(row_content)	
			 
		all_data.append(all_content)


	list=all_data#

	array=[]
	for z in list:

		list3=z[2][2:-2]
		list2=[]
		list4=[]
	
		for x in z:
			if x[1]=="Y":
				dict1=dict()
				for n in range(len(list3)):
					dict1[list3[n]]=x[2:-2][n]
				list2.append((dict1,x[-2],x[-1]))
				#print list2

		list4.append(list2)
		list4.append(z[1][1])
		list4.append(z[0][1])
		#print list4
		array.append(list4)

	sheets=[]

	for x in range(len(array)):
		sheets.append(sheetnames[x])
		#print list4

	data=[]
	for c in array:
		data.append(c+[sheets[array.index(c)]])
	return data

def gettime():
	time_now=int(time.time())
	time_local=time.localtime(time_now)
	dt=time.strftime("%Y-%m-%d %H~%M~%S",time_local)
	return dt
	
#print getdata(r'C://Users//user//Desktop//Api-automation//Apidata.xls')

					