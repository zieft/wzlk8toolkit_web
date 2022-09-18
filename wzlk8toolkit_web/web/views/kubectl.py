from django.http import JsonResponse

from utils.kubectl import KubectlDescribe, KubectlApply


def describe_pods(request, project_id):
    describe = KubectlDescribe(request)
    describe.pods()
    return JsonResponse({'stdout': describe.stdout})


def kubectl_apply_file(request, project_id):
    # todo: check if job already created
    apllier = KubectlApply(request)
    apllier.file()
    return JsonResponse({'stdout': apllier.stdout, 'status': True})
