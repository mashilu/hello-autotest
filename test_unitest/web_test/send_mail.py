# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱服务器
smtpserver = 'smtp.163.com'

# 发送邮箱用户/密码
user = 'mslbuaa@163.com'
password = 'msl327528'

# 发送邮箱
sender = 'mslbuaa@163.com'

# 接收邮箱
receiver = '67162442@qq.com'

# 发送邮件主题
subject = 'Python email test'

# 发送的附件
sendfile = open('./2018-01-03 11_41_48_result.html', 'rb').read()
att = MIMEText(sendfile, 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attatchment; filename="2018-01-03 11_41_48_result.html"'

# 编写HTML类型的邮件正文
msg = MIMEMultipart('related')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'mslbuaa@163.com'
msg['To'] = '67162442@qq.com'
msg.attach(att)

# 连接发送邮件bushi
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

