import random

from django import forms
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from web import models
from web.forms.bootstrap import BootstrapForm

from django_redis import get_redis_connection


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

    # confirm_password is not defined in model.py,so that it won't be migrated into the db
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


class SendSmsFormFake(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    mobile_phone = forms.CharField(label='Mobile Phone',
                                   validators=[RegexValidator(settings.MOBILE_PHONE_VALIDATOR,
                                                              "Please enter a valid phone number"), ])

    def clean_mobile_phone(self):
        """ validation of phone number """
        mobile_phone = self.cleaned_data['mobile_phone']

        tpl = self.request.GET.get("tpl")

        exist = models.UserInfo.objects.filter(mobile_phone=mobile_phone).exists()
        if tpl == 'login':
            if not exist:
                raise ValidationError("Phone number not exists.")
        else:
            if exist:
                raise ValidationError("Phone number already exists.")

        code = random.randrange(1000, 9999)

        conn = get_redis_connection()
        conn.set(mobile_phone, code, ex=300)
        print('The verification code is：', code)

        return mobile_phone
