from django.urls import path, re_path

from web.views import account, home, project, manager

urlpatterns = [
    path('index/', home.index, name='index'),
    path('register/', account.register, name='register'),
    path('send/sms/', account.send_sms_fake, name='send_sms'),
    path('login/', account.login, name='login'),
    path('login/sms/', account.login_sms, name='login_sms'),
    path('logout/', account.logout, name='logout'),
    path('image/code/', account.image_code, name='image_code'),

    path('project/list/', project.project_list, name='project_list'),
    re_path(r'project/star/(?P<project_type>\w+)/(?P<project_id>\d+)/$', project.project_star, name='project_star'),
    re_path(r'project/unstar/(?P<project_type>\w+)/(?P<project_id>\d+)/$', project.project_unstar,
            name='project_unstar'),

    re_path(r'^manager/(?P<project_id>\d+)/dashboard/$', manager.dashboard, name='dashboard'),
    re_path(r'^manager/(?P<project_id>\d+)/dashboard/describepods/$', manager.describe_pods, name='describe_pods'),

    re_path(r'^manager/(?P<project_id>\d+)/setting/$', manager.setting, name='setting'),
    re_path(r'^manager/(?P<project_id>\d+)/docs/$', manager.docs, name='docs'),

]
