from django.shortcuts import render


def project_list(request):
    """ project list """

    return render(request, 'project_list.html')