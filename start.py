#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json,io,sys,unittest
from readexcel import getdata
from runapi import testapi
from writehtml import returnreport
from sendemail import sendreport
from writehtml import testreport,content,write,bottom
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
#sys.setdefaultencoding('utf-8')
environment="dev-qihu-360-k5h5vl"
suffix=".kdqugou.com"
if environment[0:3]=="dev":
	env=environment+".dev"+suffix
elif environment[0:4]=="test":
	env=environment+".test"+suffix
elif environment=="stage":
	env=environment+suffix
elif environment=="jsqb":
	env=environment+suffix
write(message)
file=['C://Users//user//Desktop//Api-automation//Apidata.xls']
list=[]
if len(file)==1:
		list=getdata(file[0])
else:
		for x in file:
			list=list+getdata(x)

testapi("http://"+env,list)
sendreport("865349382@qq.com",returnreport())



	
