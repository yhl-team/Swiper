import random

import requests

from swiper import config

# 生成验证码
def gen_vcode(length=6):
    vcode = ""
    for _ in range(length):
        vcode += str(random.randint(0,9))
    return vcode


# 发送短信
def send_sms(phone,vcode):

    # 发送请求
    params = config.YZX_SMS_PARAMS.copy()
    params['param'] = vcode
    params['mobile'] = phone
    res = requests.post(config.YZX_SMS_API,json=params)
    print(res.text)
    if res.status_code == 200:
        result = res.json()
        if result['code'] == '000000':
            print('短信发送成功～！@')
        else:
            print('短信发送失败')

def send_vcode(phone):
    # 生成验证码
    vcode = gen_vcode()
    print("vcode:",vcode )
    # 发送短信
    send_sms(phone,vcode)