from django import setup
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wzlk8toolkit_web.settings")
setup()

from web import models


class FakeTracer:
    def __init__(self):
        self.project = None


class FakeRequest:
    tracer = FakeTracer()

    def __init__(self):
        self.tracer.project = None


request = FakeRequest()
request.tracer.project = models.Project.objects.filter(id=1).first()
