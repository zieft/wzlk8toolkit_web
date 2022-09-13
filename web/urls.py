from django.urls import path

from web.views import account, home, project

urlpatterns = [
    path('index/', home.index, name='index'),
    path('register/', account.register, name='register'),
    path('send/sms/', account.send_sms_fake, name='send_sms'),
    path('login/', account.login, name='login'),
    path('logout/', account.logout, name='logout'),
    path('image/code/', account.image_code, name='image_code'),

    path('project/list/', project.project_list, name='project_list'),

]
