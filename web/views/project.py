from django.http import JsonResponse
from django.shortcuts import render

from web import models
from web.forms.project import ProjectModelForm


def project_list(request):
    """ project list """
    if request.method == 'GET':
        project_dict = {'star': [], 'my': [], 'join': []}

        my_project_list = models.Project.objects.filter(  # Project object
            creator=request.tracer.user
        )
        for project in my_project_list:
            if project.star:
                project_dict['star'].append(project)
            else:
                project_dict['my'].append(project)

        join_project_list = models.ProjectUser.objects.filter(  # ProjectUser object
            user=request.tracer.user
        )
        for project_user in join_project_list:
            if project_user.star:
                project_dict['star'].append(project_user.project)
            else:
                project_dict['join'].append(project_user.project)

        form = ProjectModelForm(request)
        return render(request, 'project_list.html', {'form': form})

    form = ProjectModelForm(request, data=request.POST)
    if form.is_valid():
        form.instance.creator = request.tracer.user  # set current user as the creator of the task

        form.save()  # write to the db
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'error': form.errors})
