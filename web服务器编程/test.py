from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def web():
    return render_template('test.html')


app.run(host='127.0.0.1', port=8000, debug=False, threaded=True)
