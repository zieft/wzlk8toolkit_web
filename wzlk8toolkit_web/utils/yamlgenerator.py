import os

from django.template import Context, Engine

from web import models


class YamlGenerator:
    """ called in view function in order to pass in the request object."""

    def __init__(self, request):
        self.project = request.tracer.project
        self.task_name = request.tracer.project.name
        self.name_space = request.tracer.project.name_space

        self.rewrite_template_suffixes = (('.yaml-tpl', '.yaml'),)

        self.yamlfile = None

    def handle(self, **fields):
        context = Context({
            **fields,
            'task_name': self.project.name,
            'wzlk8toolkit_web_version': 'v0.1',
            'name_space': self.project.name_space,
        }, autoescape=False)

        try:
            os.mkdir('temp/')
        except FileExistsError:
            pass

        old_path = 'conf/yaml-template/job.yaml-tpl'

        new_path = 'temp/{}.yaml'.format(self.project.name)

        with open(old_path, encoding='utf-8') as template_file:
            content = template_file.read()

        template = Engine().from_string(content)
        content = template.render(context)
        with open(new_path, 'w', encoding='utf-8') as new_file:
            new_file.write(content)

        self.yamlfile = new_path
        # write yaml file path into db, for later use
        models.Project.objects.filter(id=self.project.id).update(yaml=self.yamlfile)
