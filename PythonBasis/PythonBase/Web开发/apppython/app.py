#pip3 install flask
from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'
@app.route('/signin',methods=['GET'])
def sifnin_from():
    return '''<from action="/signin" method="post">
    <p><input name="username"></p>
    <p><input name="passwprd" type="password"></p>
    <p><button type="submit">Sign In</button></p>
    </from>'''
@app.route('/signin',methods=['POST'])
def signin():
    if request.from['username']=='admin' and request.from['password']=='password':
        return '<h3>Hello,admin!</h3>'
    return '<h3>Bad userbname or password.</h3>'

if __name__ =="__main__":
    app.run()