#!/usr/bin/python
# -*- coding: utf-8 -*-

import xlrd
import sys
import traceback
from datetime import datetime
from xlrd import xldate_as_tuple
import requests
import json,io,sys

reload(sys)
sys.setdefaultencoding('utf-8')
class excelHandle:
    def decode(self, filename, sheetname):
        try:
            filename = filename.decode('utf-8')
            sheetname = sheetname.decode('utf-8')
        except Exception:
            print traceback.print_exc()
        return filename, sheetname

    def read_excel(self, filename, sheetname):
        filename, sheetname = self.decode(filename, sheetname)
        rbook = xlrd.open_workbook(filename)
        print rbook.sheet_names()#,sheetname
        sheet = rbook.sheet_by_name(sheetname)
        rows = sheet.nrows
        cols = sheet.ncols
        all_content = []
        for i in range(rows):
            row_content = []
            for j in range(cols):
                ctype = sheet.cell(i, j).ctype  # 表格的数据类型
                cell = sheet.cell_value(i, j)
                if ctype == 2 and cell % 1 == 0:  # 如果是整形
                    cell = int(cell)
                elif ctype == 3:
                    # 转成datetime对象
                    date = datetime(*xldate_as_tuple(cell, 0))
                    cell = date.strftime('%Y/%d/%m %H:%M:%S')
                elif ctype == 4:
                    cell = True if cell == 1 else False
                row_content.append(cell)
            all_content.append(row_content)
            #print '{' + ','.join("'" + str(element) + "'" for element in row_content) + '}'
        return all_content

        


if __name__ == '__main__':
    eh = excelHandle()
    filename = r'C://Users//user//Desktop//Api-automation//d.xls'
    sheetname = 'Sheet1'
    list=eh.read_excel(filename, sheetname)
    #print list
    #print list[1][1]
    n=len(list)
    #print len(list)
    list3=list[2][2:-2]
    #print list[2][2:-2]
    #print list3
    list4=list[3]
    #print list3
    #print list
    array=[]
    list5=[]
    for y in list:
        #print y[:-1]
        list5.append(y[:-1])
    print list5
    #print list3
    for x in list:
        #print x
        if x[1]=='Y':
            #print x[2:-1:]			
            dict1=dict()
 			
            for i in range(len(list3)):#[1:]
                dict1[list3[i]]=x[2:-2][i]
              			                
            array.append((dict1,x[-2]))	
    print array#+[list[1][1]]+[list[0][1]]
	
    print len(array)
    url=str(list[0][1])
    for x in array:
        r = requests.post(url, data=x[0])
        #print r.cookies
        print r.text
		
		
#[[u'url', u'http://dev-210-daily-opt-d64mpn.dev.kdqugou.com/credit/web/credit-user/login', u'', u'', u'', u'', u'', u'', u''], [u'requesttype', u'post', u'', u'', u'', u'', u'', u'', u''], [u'CaseID', u'Run', u'clientType', u'appVersion', u'deviceId', u'deviceName', u'osVersion', u'appMarket', u'username'], [1, u'Y', u'android', u'2.4.0.5', u'862758035226562', u'vivoX7', u'5.1.1', u'jsqb_baidu', 15138460851L], [2, u'N', u'android', u'2.4.0.5', u'862758035226562', u'vivoX7', u'5.1.1', u'jsqb_baidu', 18625990211L]]
 
	
	

	
	
