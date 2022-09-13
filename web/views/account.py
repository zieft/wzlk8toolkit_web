from django.shortcuts import render
from django.http import JsonResponse
from web.forms.account import RegisterModelForm, SendSmsFormFake

from django_redis import get_redis_connection


def register(request):
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, 'register.html', {'form': form})

    form = RegisterModelForm(data=request.POST)
    if form.is_valid():
        instance = form.save()

        return JsonResponse({'status': True, 'data': '/login/'})
    return JsonResponse({'status': False, 'error': form.errors})


def send_sms_fake(request):
    """
        A placeholder function, generate verification code and store in redis.
        The verification code can be read from the console of you browser after pressing 'Get code' button.
    """

    form = SendSmsFormFake(request, data=request.GET)
    if form.is_valid():
        conn = get_redis_connection()
        code = conn.get(form.cleaned_data.get('mobile_phone')).decode('utf-8')
        return JsonResponse({'status': True, 'code': code})  # 'code' should not be sent to the frontend

    return JsonResponse({'status': False, 'error': form.errors})
