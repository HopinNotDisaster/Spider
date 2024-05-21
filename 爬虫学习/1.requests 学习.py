import requests


def get_index():
    url = "http://127.0.0.1:5000/"
    res = requests.get(url)
    print(res)


# get_index()


def get_params():
    url = "http://127.0.0.1:5000/params?page=10&age=18"
    res = requests.get(url=url, params={"size": 20, "abcd": 1234})
    # print("请求的头部：", res.request.headers)
    print(res.json())

    # return


# get_params()

def get_data():
    url = "http://127.0.0.1:5000/data"
    res = requests.post(url=url, data={
        "name": "12", "asf": 45
    })
    # print("请求的头部：", res.request.headers)
    print(res.text)

    # return


def get_headers():
    url = "http://127.0.0.1:5000/headers"
    res = requests.get(url=url)
    print("请求的头部：", res.request.headers)
    print(res.text)

    # return


# 关于cookie有两种写法！
#   a.在headers中写入Cookie
#   b.与headers同级别的写上Cookies


def get_login():
    url = 'http://127.0.0.1:5000/login'
    res = requests.post(url=url, json={
        "username": "admin",
        "password": "123456"
    })
    return res.cookies
    # print(res)


# get_login()


def get_center(cookies):
    url = 'http://127.0.0.1:5000/center'
    res = requests.get(url=url, cookies=cookies)
    print(res.text)


# get_center(get_login())


def get_cookiesandcenter():
    session = requests.Session()
    session.post(url='http://127.0.0.1:5000/login', json={
        "username": "admin",
        "password": "123456"
    })

    res = session.get('http://127.0.0.1:5000/center')
    print(res.text)


get_cookiesandcenter()
