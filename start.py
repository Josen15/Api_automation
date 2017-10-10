#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json,io,sys,unittest
from readexcel import getdata
from runapi import testapi
from writehtml import returnreport
from sendemail import sendreport
reload(sys)
#sys.setdefaultencoding('utf-8')
environment="dev-347-bind-card-ja3a0u"
suffix=".kdqugou.com"
if environment[0:3]=="dev":
	env=environment+".dev"+suffix
elif environment[0:4]=="test":
	env=environment+".test"+suffix
elif environment=="stage":
	env=environment+suffix
elif environment=="jsqb":
	env=environment+suffix

testapi("http://"+env,getdata(r'C://Users//user//Desktop//Api-automation//Apidata.xls'))
#print returnreport()
sendreport("865349382",returnreport())
#testapi("http://dev-210-daily-opt-d64mpn.dev.kdqugou.com",getdata(r'C://Users//user//Desktop//Api-automation//Apidata.xls'))


	