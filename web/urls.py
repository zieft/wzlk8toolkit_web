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
    path(r'project/star/(?P<project_type>\w+)/(?P<project_id>\d+)/$', project.project_star, name='project_star'),
    path(r'project/unstar/(?P<project_type>\w+)/(?P<project_id>\d+)/$', project.project_unstar, name='project_unstar'),

]
