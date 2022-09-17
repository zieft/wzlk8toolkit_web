from django.http import JsonResponse

from utils.kubectl import KubectlDescribe, KubectlApply


def describe_pods(request, project_id):
    describe = KubectlDescribe(request)
    describe.pods()
    return JsonResponse({'stdout': describe.stdout})


def kubectl_apply(request, project_id):
    aplly = KubectlApply()
    aplly.file()
