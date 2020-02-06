import json
import re
import hashlib
import requests
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def parse_xml(string):
    return list(map(lambda x: x[6:-2], re.findall('CDATA\[.*\]', string)))


def get_token(event, content):
    if event["requestContext"]["httpMethod"] != "GET":
        return {"errorCode": 413, "errorMsg": "request is not correctly execute"}
    if "requestContext" not in event.keys():
        return {"errorCode": 410, "errorMsg": "event is not come from api gateway"}
    try:
        signature = event['queryString']['signature']
        timestamp = event['queryString']['timestamp']
        nonce = event['queryString']['nonce']
        echostr = event['queryString']['echostr']
        token = "myToken"

        li = [token, timestamp, nonce]
        li.sort()
        tmp = li[0] + li[1] + li[2]
        sha1 = hashlib.sha1()
        sha1.update(tmp.encode())
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            return echostr.encode()
        else:
            return "".encode()
    except Exception as Argument:
        return Argument


def get_access_token(appid, secret,grant_type='client_credential'):
    api = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=%s&appid=%s&secret=%s'
    text = requests.get(api % (grant_type, appid, secret)).text
    print(text)
    try:
        access_token = json.loads(text)['access_token']
        return access_token
    except Exception as e:
        print(e)
        return ''


my_sender = 'LanceLiang2018@163.com'  # 发件人邮箱账号
my_pass = '1352040930smtp'  # 发件人邮箱密码
# my_user = '1352040930@qq.com'  # 收件人邮箱账号


# 好像没法主动发消息。。
def send_message(toUserName, fromUserName, msgType, content: str):
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr([toUserName, my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([fromUserName, my_sender])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "来自微信公众号的新消息"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_sender, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:
        print(e)


def handle(event, content):
    if event['httpMethod'] == 'GET':
        return get_token(event, content)
    elif event['httpMethod'] == 'POST':
        data = parse_xml(event['body'])
        send_message(data[0], data[1], data[2], data[3])
    return ''


# if __name__ == '__main__':
#     ac = get_access_token('wxc85c1fea1fe99496', '29708b48caa4452fd45c32f51fbfdf58')
#     print(ac)

'''
<xml><ToUserName><![CDATA[gh_7a615f0a70b0]]></ToUserName>\n<FromUserName><![CDATA[oeGkQs8vaMYPZ5CQUnmhTR5u1Lww]]></FromUserName>\n<CreateTime>1580969759</CreateTime>\n<MsgType><![CDATA[text]]></MsgType>\n<Content><![CDATA[\u7f8e\u4e2d\u4e0d\u8db3\u5ac1\u9e21\u968f\u9e21\u60f3\u4f60]]></Content>\n<MsgId>22634044114590692</MsgId>\n</xml>
'''
