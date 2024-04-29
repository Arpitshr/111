# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
import psutil
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/showprocess1')
def show_p():
    pids = psutil.pids()
    process= {}
    for pid in pids:
        p = psutil.Process(pid)
        process.update({pid:p.name()})
    return process

if __name__ == '__main__':
    app.run(host="0.0.0.0")

