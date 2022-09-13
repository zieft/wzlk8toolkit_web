from django import forms
from web.forms.bootstrap import BootstrapForm
from web import models


class ProjectModelForm(BootstrapForm, forms.ModelForm):
    # desc = forms.CharField(widget=forms.Textarea(attrs={'xx': 123})) # apply Textarea style to CharField

    class Meta:
        model = models.Project
        fields = ['name', 'color', 'bucket', 'S3_key', 'S3_secret_key', 'desc']

        widgets = {
            'desc': forms.Textarea(attrs={'xx': 123}),
            'S3_secret_key': forms.PasswordInput,
        }
