#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import requests
import json,io,sys,unittest,time

from readexcel import getdata
from writehtml import testreport,content,write,bottom,total,bottom1
reload(sys)
sys.setdefaultencoding('utf-8')
#GEN_HTML = "%s APItestreport1.html" %(time.time())
#f = open(GEN_HTML,'w')

message = """
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset="utf-8" /> 
		<title></title>
		<script src="http://code.jquery.com/jquery-1.4.1.js"></script>
	</head>
	<style>
		table
     {
     	align:left
     	margin:0 auto;
         border-collapse :collapse ;
     }
     th,td
     {
         width:500px;
         height:40px;
         border :1px solid black;
         font-size:12px;
         text-align :center;
		 word-break:break-all; /*支持IE，chrome，FF不支持*/
		 word-wrap:break-word;/*支持IE，chrome，FF*/
     }
    .show{
         color:black;
     }
     h1{
         position:relative;
     }
     .tj{
         position:absolute;
         top:60px;
         right:30px;
     }
     .tj p{
         display:inline-block;
     }
	</style>
	<body>
		<h1 align="center">极速钱包接口测试报告</h1>
		<div>
		
			


	"""

def testapi(env,status):
	t=0
	p=0
	f=0
	tim=0.00
	list=status
	#print len(list)
	cookielist=[]
	
	#write(message)
	for x in list:

		write(testreport(x[-2]))
		if x[-1]=="login":
			logindata=x[:-3]		
			url=env+x[-2]
			for y in logindata:
				#print x[-1]
				
				for i in y:
					list1=[]
					start_time = time.time()
					postresponse = requests.post(url, data=i[0])
					responsetime= time.time()-start_time
					t = t + 1
					tim=tim+float('%.2f'%responsetime)

					code=json.loads(postresponse.text.encode('utf-8'))["code"]
					list1.append(i[2])
					list1.append(postresponse.status_code)
					list1.append('%.2f'%responsetime)
					if i[1]==code:
						#print i[2]+'  测试  '+u'通过'
						#print  '%.2f'%responsetime
						p=p+1
						list1.append(u"<p>通过")
						list1.append("<p class='show' style='display: none;'>"+postresponse.text+"</p>")
						if code==0:
							cookielist.append(postresponse.cookies)
						
					else:
						f=f+1
						#print postresponse.text
						list1.append(u"<p style='color:red;'>不通过")
						list1.append("<p class='show' style='display: none;'>"+postresponse.text+"</p>")
					
					write(content(list1))
		else:
			requestdata=x[:-3]		
			site=env+x[-2]
			for y in requestdata:
				#print x[-1]
				for i in y:
			
					if x[-3]=="get":
						list2=[]
						start_time = time.time()
						getresponse = requests.get(site,params=i[0],cookies=cookielist[0])
						responsetime= time.time()-start_time
						t = t + 1
						tim=tim+float('%.2f'%responsetime)
						code=json.loads(getresponse.text.encode('utf-8'))["code"]
						list2.append(i[2])
						list2.append(getresponse.status_code)
						list2.append('%.2f'%responsetime)
						if i[1]==code:
							p=p+1
							list2.append(u"<p>通过")
							list2.append("<p class='show' style='display: none;'>"+getresponse.text+"</p>")
							#print i[2]+'  测试  '+u'通过'
						else:
							f=f+1
							#print getresponse.text
							list2.append(u"<p style='color:red;'>不通过")
							list2.append("<p class='show' style='display: none;'>"+getresponse.text+"</p>")
						
						write(content(list2))
					else:
						list3=[]
						start_time = time.time()
						postreturn = requests.get(site,params=i[0],cookies=cookielist[0])
						responsetime= time.time()-start_time
						t = t + 1
						tim=tim+float('%.2f'%responsetime)
						code=json.loads(postreturn.text.encode('utf-8'))["code"]
						list3.append(i[2])
						list3.append(postreturn.status_code)
						list3.append('%.2f'%responsetime)
						if i[1]==code:
							#print i[2]+'  测试  '+u'通过'
							p=p+1
							list3.append(u"<p>通过")
							list3.append("<p class='show' style='display: none;'>"+postreturn.text+"</p>")
							
						else:
							f=f+1
							#print postreturn.text
							list3.append(u"<p style='color:red;'>不通过")
							list3.append("<p class='show' style='display: none;'>"+postreturn.text+"</p>")
							
						write(content(list3))
	bottom1()
	write(total(t,p,f,'%.2f%%' % ((p/t) * 100),'%.2f'%(tim/t)))
	bottom()

							
							
					

#testapi("http://dev-ps-900-index-pid0sl.dev.kdqugou.com",getdata(r'C://Users//user//Desktop//Api-automation//Apidata.xls'))
						
						

			

		

		
	
		