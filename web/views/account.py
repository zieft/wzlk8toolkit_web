from django.shortcuts import render, HttpResponse
from web.forms.account import RegisterModelForm
from web.forms.bootstrap import BootstrapForm


def register(request):
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})
