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
        if url in white_list:
            return  # middleware returns None, means do nothing, program will continue

        # Check if user is logged in, if not, redirect to 'login' page.
        if not request.tracer.user:
            return redirect('login')
