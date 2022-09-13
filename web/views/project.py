from django.http import JsonResponse
from django.shortcuts import render

from web.forms.project import ProjectModelForm


def project_list(request):
    """ project list """
    if request.method == 'GET':
        form = ProjectModelForm(request)
        return render(request, 'project_list.html', {'form': form})

    form = ProjectModelForm(request, data=request.POST)
    if form.is_valid():
        form.instance.creator = request.tracer.user  # set current user as the creator of the task

        form.save()  # write to the db
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'error': form.errors})
