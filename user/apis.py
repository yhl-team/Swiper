from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from lib.sms import send_vcode,check_vcode

# Create your views here.
#api
def submit_vcode(request):
    # 发送验证码
    phone = request.GET.get('phone')

    # 发送验证码
    result = send_vcode(phone)
    print('--------------------')
    print(result)
    return JsonResponse({'msg':result})


#登录
def login(request):
    #获取前端数据
    phone = request.POST.get('phone')
    vcode = request.POST.get('vcode')

    if check_vcode(phone,vcode):
        print('登录成功！@～')


    return JsonResponse({'msg':'ok'})