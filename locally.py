import hashlib
from flask import *


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
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
            return str(Argument)
    elif request.method == 'POST':
        print('Got a post!')
        return ''


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=False)
