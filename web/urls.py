from django.urls import path

from web.views import account, home

urlpatterns = [
    path('index/', home.index, name='index'),
    path('register/', account.register, name='register'),
]
