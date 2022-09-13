import random

from django import forms
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from web import models
from web.forms.bootstrap import BootstrapForm
from utils import encrypt

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

    mobile_phone = forms.CharField(label="Mobile Phone",
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

    def clean_username(self):
        username = self.cleaned_data['username']

        exists = models.UserInfo.objects.filter(username=username).exists()

        if exists:
            self.add_error('username', 'Username already exists!')

        return username

    def clean_password(self):
        pwd = self.cleaned_data['password']

        return encrypt.md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')

        cfm_pwd = encrypt.md5(self.cleaned_data['confirm_password'])
        if pwd != cfm_pwd:
            raise ValidationError('Passwords do not match.')
        return cfm_pwd

    def clean_mobile_phone(self):
        mobile_phone = self.cleaned_data['mobile_phone']
        exists = models.UserInfo.objects.filter(mobile_phone=mobile_phone).exists()
        if exists:
            raise ValidationError('Phone number already exists.')
        return mobile_phone

    def clean_code(self):
        code = self.cleaned_data['code']
        mobile_phone = self.cleaned_data.get('mobile_phone')
        if not mobile_phone:
            return code
        conn = get_redis_connection()
        redis_code = conn.get(mobile_phone)
        if not redis_code:
            raise ValidationError('Verification code is not valid, please try again!')

        redis_str_code = redis_code.decode('utf-8')

        if redis_str_code.strip() != code:
            raise ValidationError('Verification code is wrong, please try again!')

        return code


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


class LoginForm(BootstrapForm, forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput(render_value=True))
    code = forms.CharField(label='Code')

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_password(self):
        pwd = self.cleaned_data['password']

        return encrypt.md5(pwd)

    def clean_code(self):
        # get user input
        code = self.cleaned_data['code']

        # get
        code_from_session = self.request.session.get("image_code")
        if not code_from_session:
            raise ValidationError("Code is expired, please try again")

        if code.upper().strip() != code_from_session.upper().strip():
            raise ValidationError("Wrong code.")

        return code
