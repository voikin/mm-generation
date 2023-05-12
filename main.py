from flask import Flask, Response
app = Flask(__name__)


@app.route('/list')
def get_list():
    return Response([], 200)


@app.route('/ration')
def get_ration():
    return Response([], 200)


if __name__ == '__main__':
    app.run()