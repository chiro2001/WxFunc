from flask import *


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def test():
    return ''


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=False)
