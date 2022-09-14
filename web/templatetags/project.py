from django.template import Library

from web import models

register = Library()

"""
inclusion_tag pack the often used code block
"""


@register.inclusion_tag('inclusion/all_project_list.html')
def all_project_list(request):  # this is not a view function, so request parameter needs to be pass in manually
    # 1. acquire all tasks created by me
    my_project_list = models.Project.objects.filter(creator=request.tracer.user)

    # 2. acquire all tasks I participate
    join_project_list = models.ProjectUser.objects.filter(user=request.tracer.user)

    return {'my': my_project_list, 'join': join_project_list, 'request': request}
    # direct pass return value to the .html file inclusion/all_project_list.html
