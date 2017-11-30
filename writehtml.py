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
      <td  class="result">%s</p>%s</td>
    </tr>
	'''%(list[0],list[1],list[2],list[3],list[4])
	return mid
def total(a,b,c,d,e):
	total='''
		<div class="tj">
            <p>测试接口总数：%s </p>
            <p>测试通过总数：%s </p>
            <p>测试失败总数：%s </p>
            <p>通过率：%s </p>
            <p>平均响应时间：%s s</p>
        </div>	
		'''%(a,b,c,d,e)
	return total

def write(middle):
	
	f.write(middle)
def bottom1():
	bot1 = """
      </table>
    	</div>

    </body>
    """
	write(bot1)
def bottom():
	
	bot="""
		<script>
		$('.result').click(function(){
			if($(this).find('.show').attr('style') == 'display: none;'){
				$(this).find('.show').show();
			}else{
				$(this).find('.show').hide();
			}
		})
	</script>
</html>
"""
	write(bot)
def returnreport():
	return "C:\\Users\\user\\Desktop\\Api-automation\\"+GEN_HTML
	#webbrowser.open(GEN_HTML,new = 1)
 

	
	



