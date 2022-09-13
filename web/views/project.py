from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

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
                project_dict['star'].append({'value': project, 'type': 'my'})
            else:
                project_dict['my'].append(project)

        join_project_list = models.ProjectUser.objects.filter(  # ProjectUser object
            user=request.tracer.user
        )
        for project_user in join_project_list:
            if project_user.star:
                project_dict['star'].append({'value': project_user.project, 'type': 'my'})
            else:
                project_dict['join'].append(project_user.project)

        form = ProjectModelForm(request)
        return render(request, 'project_list.html', {'form': form, 'project_dict': project_dict})

    form = ProjectModelForm(request, data=request.POST)
    if form.is_valid():
        form.instance.creator = request.tracer.user  # set current user as the creator of the task

        form.save()  # write to the db
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'error': form.errors})


def project_star(request, project_type, project_id):
    """ star a task """

    if project_type == 'my':
        models.Project.objects.filter(
            id=project_id,
            creator=request.tracer.user  # ensure the owner
        ).update(star=True)
        return redirect('project_list')

    if project_type == 'join':
        models.ProjectUser.objects.filter(
            project_id=project_id,
            user=request.tracer.user,  # ensure the task that I participate
        ).update(star=True)
        return redirect('project_list')

    return HttpResponse("Bad request.")


def project_unstar(request, project_type, project_id):
    """ unstar a starred task """

    if project_type == 'my':
        models.Project.objects.filter(
            id=project_id,
            creator=request.tracer.user  # ensure the owner
        ).update(star=False)
        return redirect('project_list')
    if project_type == 'join':
        models.ProjectUser.objects.filter(
            project_id=project_id,
            user=request.tracer.user,  # ensure the task that I participate
        ).update(star=False)
        return redirect('project_list')

    return HttpResponse("Bad request.")
