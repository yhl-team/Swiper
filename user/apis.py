from django.http import JsonResponse
from django.shortcuts import render
from lib.sms import send_vcode

# Create your views here.
#api
def submit_vcode(request):
    # 发送验证码
    phone = request.GET.get('phone')

    # 发送验证码
    send_vcode(phone)

    return JsonResponse({'msg':'ok'})