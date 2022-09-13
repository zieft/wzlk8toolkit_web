from django.shortcuts import render
from django.http import JsonResponse
from web.forms.project import ProjectModelForm

def project_list(request):
    """ project list """
    if request.method == 'GET':
        form = ProjectModelForm()
        return render(request, 'project_list.html', {'form': form})

    form = ProjectModelForm(data=request.POST)
    if form.is_valid():
        pass

    return JsonResponse({'status': False, 'error': form.errors})
