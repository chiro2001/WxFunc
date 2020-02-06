import hashlib
from flask import *


def get_token(event, content):
    if event["requestContext"]["httpMethod"] != "GET":
        return {"errorCode": 413, "errorMsg": "request is not correctly execute"}
    if "requestContext" not in event.keys():
        return {"errorCode": 410, "errorMsg": "event is not come from api gateway"}
    # if event["requestContext"]["path"] != "/token":
    #     return {"errorCode": 411, "errorMsg": "request is not from setting api path"}

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


app = Flask(__name__)


@app.route('/')
def test():
    args0 = dict(request.args)
    args = {}
    for arg in args0:
        val = args0[arg]
        if type(val) is list:
            args[arg] = val[0]
        else:
            args[arg] = val
    print(args)

    try:
        signature = args['signature']
        timestamp = args['timestamp']
        nonce = args['nonce']
        echostr = args['echostr']
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


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=False)
