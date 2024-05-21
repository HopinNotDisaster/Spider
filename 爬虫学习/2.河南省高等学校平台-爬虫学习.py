import requests
from ddddocr import DdddOcr


# 401 未认证，权限不够！
def get_user_info(user_token):
    url = "https://testapi.hnilab.com/api/User/GetTokenUser"
    headers = {
        'Authorization': f'Bearer {user_token}'
    }

    res = requests.get(url=url, headers=headers)
    print(res.json()['rows']['username'])


def get_user_token(keyandverifycode):
    url = 'https://testapi.hnilab.com/api/Login/Login'
    res = requests.post(url=url, json={
        'account': "17373545043",
        'password': "123456",
        'key': keyandverifycode['key'],
        'verifycode': keyandverifycode['verifycode'],
    })
    return res.json()['rows']['accesstoken']


def get_keyandverifycode():
    url = 'https://testapi.hnilab.com/api/Login/GenerateVerifyCode'
    res = requests.get(url=url)
    # print(res.json()['rows'])

    img_base64 = res.json()['rows']["codeimage"][22:]
    ocr = DdddOcr(show_ad=False)
    verifycode = ocr.classification(img_base64)
    print(verifycode)

    return {
        "key": res.json()['rows']['key'],
        'verifycode': verifycode
    }


user_token = get_user_token(get_keyandverifycode())
get_user_info(user_token)
