from django.shortcuts import render
from django.http import JsonResponse

from utils.kubectl.describe import KubectlDescribe


def dashboard(request, project_id):
    return render(request, 'dashboard.html')


def describe_pods(request, project_id):
    describe = KubectlDescribe(request)
    describe.pods()
    return JsonResponse({'stdout': describe.stdout})


def docs(request, project_id):
    return render(request, 'docs.html')


def setting(request, project_id):
    return render(request, 'setting.html')

