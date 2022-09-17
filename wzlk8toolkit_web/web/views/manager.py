from django.shortcuts import render, redirect

from utils.yamlgenerator import YamlGenerator
from web.forms.manager import SettingYamlForm


def dashboard(request, project_id):
    return render(request, 'dashboard.html')


def docs(request, project_id):
    return render(request, 'docs.html')


def setting(request, project_id):
    if request.method == "GET":
        form = SettingYamlForm()
        return render(request, 'setting.html', {'form': form})

    fields = {}
    QueryDict = request.POST
    for key in QueryDict.keys():
        fields[key] = QueryDict.get(key)


    form = SettingYamlForm(request, request.POST)

    generator = YamlGenerator(request)
    generator.handle(**fields)

    return redirect('project_list')
