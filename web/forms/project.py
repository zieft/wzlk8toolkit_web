from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from web import models
from web.forms.bootstrap import BootstrapForm


class ProjectModelForm(BootstrapForm, forms.ModelForm):
    # desc = forms.CharField(widget=forms.Textarea(attrs={'xx': 123})) # apply Textarea style to CharField
    name = forms.CharField(label='Task name',
                           validators=[RegexValidator(r"^[-a-zA-Z0-9_]+\Z",
                                                      'Please use only "a-z", "A-Z", "-", "_" and "0-9".')]
                           )

    class Meta:
        model = models.Project
        fields = ['name', 'color', 'bucket', 'S3_key', 'S3_secret_key', 'desc']

        widgets = {
            'desc': forms.Textarea(attrs={'xx': 123}),
            'S3_secret_key': forms.PasswordInput,
        }

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_name(self):
        """ task name validation """
        name = self.cleaned_data['name']
        exists = models.Project.objects.filter(name=name, creator=self.request.tracer.user).exists()
        if exists:
            raise ValidationError("Task name exists.")
        return name
