import random

import requests
from django.core.cache import cache

from swiper import config


# 生成验证码
def gen_vcode(length=6):
    vcode = ""
    for _ in range(length):
        vcode += str(random.randint(0, 9))
    return vcode


# 发送短信
def send_sms(phone, vcode):
    # 发送请求
    params = config.YZX_SMS_PARAMS.copy()
    params['param'] = vcode
    params['mobile'] = phone
    res = requests.post(config.YZX_SMS_API, json=params)
    print(res.text)
    if res.status_code == 200:
        result = res.json()
        if result['code'] == '000000':
            print('短信发送成功～！@')
            return result['msg']
        else:
            print('短信发送失败')
            return result['msg']
    else:
        return '发送短信失败!'


# 发送验证码
def send_vcode(phone):
    # 生成验证码
    vcode = gen_vcode()
    print("vcode:", vcode)

    # 缓存
    key = "VCODE-%s" % phone
    cache.set(key, vcode, 180)
    # 发送短信
    result = send_sms(phone, vcode)
    return result


# 校验短信验证码
def check_vcode(phone, vcode):
    cached_vcode = cache.get('VCODE-%s' % phone)
    return cached_vcode == vcode
