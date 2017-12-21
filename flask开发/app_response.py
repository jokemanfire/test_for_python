# coding=utf-8

from flask import Flask,jsonify
from werkzeug.wrappers import Response
app = Flask(__name__)

class JSONresponse(Response):
    @classmethod
    def force_type(cls, rv, environ=None):
        if isinstance(rv,dict):
            rv = jsonify(rv)
        return super(JSONresponse,cls).force_type(rv,environ)

app.response_class = JSONresponse

@app.route('/')
def hello_world():
    return {'message':'Hello World!'}

@app.route('/custom_headers')
def headers():
    return {'headers':[1,2,3]},201,[('X-Request-Id','100')]

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8999)