from django.shortcuts import render


def dashboard(request, project_id):
    return render(request, 'dashboard.html')


def docs(request, project_id):
    return render(request, 'docs.html')


def setting(request, project_id):
    return render(request, 'setting.html')
