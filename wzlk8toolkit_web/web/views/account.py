from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django_redis import get_redis_connection

from web import models
from web.forms.account import RegisterModelForm, SendSmsFormFake, LoginForm


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


def login(request):
    """ Username - Password Login"""
    if request.method == 'GET':
        form = LoginForm(request)
        return render(request, 'login.html', {'form': form})
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user_object = models.UserInfo.objects.filter(username=username, password=password).first()
        if user_object:
            # user exist, login successful
            request.session['user_id'] = user_object.id
            # request.session['user_name'] = user_object.username
            request.session.set_expiry(60 * 60 * 24)  # login session for 24 hours
            return redirect('project_list')
        form.add_error('username', 'Username or Password invalid!')

    return render(request, 'login.html', {'form': form})


def image_code(request):
    from utils.image_code import check_code
    from io import BytesIO
    img, code = check_code()
    request.session['image_code'] = code
    request.session.set_expiry(600)

    stream = BytesIO()
    img.save(stream, 'png')

    return HttpResponse(stream.getvalue())


def logout(request):
    request.session.flush()
    return redirect('login')
