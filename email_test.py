import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


my_sender = 'LanceLiang2018@163.com'  # 发件人邮箱账号
my_pass = '1352040930smtp'  # 发件人邮箱密码
my_user = '1352040930@qq.com'  # 收件人邮箱账号
try:
    # print('try to send:', user)
    msg = MIMEText('邮件测试', 'plain', 'utf-8')
    msg['From'] = formataddr(["Lance Liang", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr(['Lance Liang', my_sender])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = "来自 %s 的新消息"  # 邮件的主题，也可以说是标题

    server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
    server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender, [my_sender, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
except Exception as e:
    print(e)
