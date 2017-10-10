#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from writehtml import gettime
def sendreport(n,filename):
	_user = "865349382@qq.com"
	_pwd = "wibwfnhfpujjbccd"
	_to = n+"@qq.com" # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

#创建一个带附件的实例
	message = MIMEMultipart()
	message['From'] = Header("王中生", 'utf-8')#发件人名字
	#message['To'] =  Header("测试", 'utf-8')#收件名字
	subject = '极速钱包接口测试'#收件列表和详情标题
	message['Subject'] = Header(subject, 'utf-8')
 
#邮件正文内容
	message.attach(MIMEText('%s 极速钱包接口测试报告'%gettime(), 'plain', 'utf-8'))#邮件详情内容
 
# 构造附件1，传送当前目录下的 test.txt 文件
	att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
	att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
	att1["Content-Disposition"] = 'attachment; filename="jsqb_api testreport.html"'
	message.attach(att1)
 

	try:
		s = smtplib.SMTP_SSL("smtp.qq.com", 465)
		s.login(_user, _pwd)
		s.sendmail(_user, _to, message.as_string())
		s.quit()
		print "Success!"
	except smtplib.SMTPException,e:
		print "Falied,%s"%e
