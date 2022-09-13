from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(verbose_name="Username",
                                max_length=32,
                                db_index=True,
                                )

    email = models.CharField(verbose_name="E-mail",
                             max_length=32)

    # verbosename can be rewrite in ModelFomrs
    password = models.CharField(verbose_name="Password",
                                max_length=32)

    mobile_phone = models.CharField(verbose_name='Mobil phone',
                                    max_length=12)
