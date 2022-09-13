from django import forms
from django.conf import settings
from django.core.validators import RegexValidator

from web import models
from web.forms.bootstrap import BootstrapForm


class RegisterModelForm(BootstrapForm, forms.ModelForm):
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(attrs={
                                   # 'class': 'form-control',
                                   'placeholder': 'placeholder'
                               }
                               ),
                               min_length=8,
                               max_length=64,
                               error_messages={
                                   'min_length': 'Password must longer than 7 characters.',
                                   'max_length': 'Password must shorter than 65 characters.',
                               },

                               )

    # 下面的字段没有定义在model.py里，因此不会被迁移到数据库中
    confirm_password = forms.CharField(label="Confirm Password",
                                       widget=forms.PasswordInput(),
                                       min_length=8,
                                       max_length=64,
                                       error_messages={
                                           'min_length': 'Password must longer than 7 characters.',
                                           'max_length': 'Password must shorter than 65 characters.',
                                       },
                                       )

    mobile_phone = forms.CharField(label="mobile_phone",
                                   validators=[RegexValidator(settings.MOBILE_PHONE_VALIDATOR,
                                                              "Please enter a valid phone number."), ])

    code = forms.CharField(
        label='Verification Code',
        widget=forms.TextInput()
    )

    class Meta:
        model = models.UserInfo
        fields = ['username', 'email', 'password', 'confirm_password',
                  'mobile_phone', 'code']
