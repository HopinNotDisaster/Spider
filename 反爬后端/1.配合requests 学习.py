from flask import Flask, jsonify
from flask import request, session
import json

app = Flask(__name__)

app.secret_key = "sssdgsgdgssdg.sgd21gds15.es"


@app.get("/")
def index():
    return "<h1>后端反爬模拟！</h1>"


@app.get('/params')
def params():
    print(request.args, "****************")
    result = {
        "code": 0,
        "args": request.args,
        "headers": {
            "UA": request.headers["User-Agent"]
        }
    }
    return jsonify(result)


@app.post('/data')
def data():
    # print(request.args, "****************")
    result = {
        "code": 0,
        # "args": request.args,
        "data": request.form,
        "headers": {
            "UA": request.headers["User-Agent"]
        }
    }
    return jsonify(result)


@app.get("/headers")
def headers():
    if request.headers["User-Agent"].startswith('python'):
        return "不要使用python来访问我的网站！"


@app.post("/login")
def login():
    username = request.json.get("username", None)
    password = request.json["password"]
    print(username, password, "*****************")

    session["user"] = json.dumps({
        'username': username,
        "VIP": "18"
    })

    result = {
        "code": 0,
        "msg": "登录成功！"
    }
    return jsonify(result)


@app.get("/center")
def center():
    user = session.get("user")
    if user:
        result = {
            "code": 0,
            "msg": "欢迎来到center！"
        }
    else:
        result = {
            "code": -1,
        }

    return jsonify(result)


app.run(debug=True)
