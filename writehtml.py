#!/usr/bin/env python
#  -*- coding:utf-8 -*-



import webbrowser
import time
from readexcel import gettime
 #命名生成的html

 
GEN_HTML = "%s APItestreport.html" %(gettime())
#print "C:\\Users\\user\\Desktop\\Api-automation\\%s"%GEN_HTML
f = open("C:\\Users\\user\\Desktop\\Api-automation\\%s"%GEN_HTML,'w')


	

def testreport(head):
	report="""

<table>
	<h2 style="text-align:left ">%s</h2>
    <tr>
      <th style="background : darkgreen;">用例描述</th>
      <th style="background: darkgreen;">响应值code</th>
      <th style="background: darkgreen;">响应时间</th>
      <th style="background: darkgreen;">测试结果</td>
    </tr>

"""%head
	return report
def content(list):
	mid='''
	<tr>
      <td>%s</td>
      <td>%s</td>
	  <td>%s</td>
      <td>%s</td>
    </tr>
	'''%(list[0],list[1],list[2],list[3])
	return mid


def write(middle):
	
	f.write(middle)
def bottom():
	
	bot="""
	  </table>
		</div>
	</body>
</html>
"""
	write(bot)
def returnreport():
	return "C:\\Users\\user\\Desktop\\Api-automation\\"+GEN_HTML
	#webbrowser.open(GEN_HTML,new = 1)
 

	
	



