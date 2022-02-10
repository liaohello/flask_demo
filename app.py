from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index2():  # put application's code here
    return render_template("index.html")

@app.route('/index')
def hello():
    return 'Hello'

@app.route('/user/<name>')
def welcom(name):
    return 'Hellol,%s'%name

@app.route('/user/<int:id>')
def welcom2(id):
    return 'Hellol,%d号的会员'%id

if __name__ == '__main__':
    app.run(debug = True)
