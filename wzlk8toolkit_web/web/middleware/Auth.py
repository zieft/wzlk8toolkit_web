from django.conf import settings
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from web import models


class Tracer(object):
    def __init__(self):
        self.user = None
        self.project = None


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        If user is logged in，then write a value into request object.
        For instance：
        request.tracer = 666
        so，when a user successfully logged in，request.tracer can be reached from any view functions.
        """
        request.tracer = Tracer()

        user_id = request.session.get('user_id', 0)  # get username from session, 0 if not exists

        user_object = models.UserInfo.objects.filter(id=user_id).first()
        request.tracer.user = user_object

        # white list：can be viewed without login.
        white_list = settings.WHITE_REGEX_URL_LIST
        # get user requested url
        url = request.path_info
        # check if in white list
        for white_url in white_list:
            if not url.startswith(white_url):
                continue
            return  # middleware returns None, means do nothing, program will continue

        # Check if user is logged in, if not, redirect to 'login' page.
        if not request.tracer.user:
            return redirect('login')

    def process_view(self, request, view, args, kwargs):
        """
        Before entering this middleware，make sure url validation is passed.
        Otherwise, project_id cannot be acquired properly.
         """

        # 1 if url start with 'manager'
        if not request.path_info.startswith('/manager'):
            return  # return 表示验证通过，继续往下走第2步

        # 1.5 acquire project_id and user object
        project_id = kwargs.get('project_id')
        user_object = request.tracer.user

        # 2. check if the project is created by me
        project_object = models.Project.objects.filter(
            creator=user_object,
            id=project_id
        ).first()

        if project_object:  # if created by me
            request.tracer.project = project_object
            return

        # 2.5 if not created by me, it could be a task which I participated
        project_user_object = models.ProjectUser.objects.filter(
            user=request.tracer.user,
            project_id=project_id
        ).first()

        if project_user_object:  # if I participated
            request.tracer.project = project_user_object.project
            return

        # 3 None of above conditions satisfied, redirect to 'project_list'
        return redirect('project_list')
