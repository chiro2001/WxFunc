import hashlib


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


# if __name__ == '__main__':
#     _event = {
#         "headerParameters": {},
#         "headers": {
#             "accept": "*/*",
#             "connection": "Keep-Alive",
#             "host": "wx.lanceliang2001.top",
#             "pragma": "no-cache",
#             "user-agent": "Mozilla/4.0",
#             "x-anonymous-consumer": "true",
#             "x-qualifier": "$LATEST"
#         },
#         "httpMethod": "GET",
#         "path": "/token",
#         "pathParameters": {},
#         "queryString": {
#             "echostr": "1142829501818863613",
#             "nonce": "1421350532",
#             "signature": "548802ddca844cfb5106f76f8d5c649755c611aa",
    #             "timestamp": "1580924925"
#         },
#         "queryStringParameters": {
#             "echostr": "1142829501818863613",
#             "nonce": "1421350532",
#             "signature": "548802ddca844cfb5106f76f8d5c649755c611aa",
#             "timestamp": "1580924925"
#         },
#         "requestContext": {
#             "httpMethod": "GET",
#             "identity": {},
#             "path": "/token",
#             "serviceId": "service-6ak1eo86",
#             "sourceIp": "223.166.222.118",
#             "stage": "release"
#         }
#     }
#     print(get_token(_event, None))

