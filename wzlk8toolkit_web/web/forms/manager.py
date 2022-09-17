from django import forms

from web.forms.bootstrap import BootstrapForm

class SettingYamlForm(BootstrapForm, forms.Form):
    pvc_space_receive = forms.IntegerField(label='Space for "Storage" (50-150)', max_value=150, min_value=50,
                                           initial=100)
    pvc_space_send = forms.IntegerField(label='Space for "Send" (50-150)', max_value=150, min_value=50,
                                        initial=150)
    image_name = forms.CharField(label='Backend Image', initial='zieft/wzl_k8toolkit:latest')
    container_port = forms.IntegerField(label='Container Port (19000-19999)', max_value=19999, min_value=19000,
                                        initial=19001)
    cpu_power = forms.IntegerField(label='CPU in cores (1-16)', max_value=16, min_value=1, initial=4)

    memory = forms.IntegerField(label='Memory in Gi (1-64)', max_value=64, min_value=1, initial=32)
