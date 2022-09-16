from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class UserInfo(AbstractUser):
    # username = models.CharField(verbose_name="Username",
    #                             max_length=32,
    #                             db_index=True,
    #                             )

    # email = models.CharField(verbose_name="E-mail",
    #                          max_length=32)

    # verbosename can be rewrite in ModelFomrs
    # password = models.CharField(verbose_name="Password",
    #                             max_length=32)

    mobile_phone = models.CharField(verbose_name='Mobil phone',
                                    max_length=12)


class Project(models.Model):
    """ Project table """
    COLOR_CHOICES = (
        (1, '#56b8eb'),
        (2, '#f28033'),
        (3, '#ebc656'),
        (4, '#a2d148'),
        (5, '#20BFA4'),
        (6, '#7461c2'),
        (7, '#20bfa3'),
    )

    name = models.CharField(verbose_name='Task Name', max_length=32)
    color = models.SmallIntegerField(verbose_name='Color', choices=COLOR_CHOICES, default=1)
    desc = models.CharField(verbose_name='Description', max_length=255, null=True, blank=True)
    use_space = models.IntegerField(verbose_name='Space used', default=0)
    star = models.BooleanField(verbose_name='Star', default=False)

    join_count = models.SmallIntegerField(verbose_name='Number of participants', default=1)
    creator = models.ForeignKey(verbose_name='Creator', to='UserInfo', on_delete=models.CASCADE)
    create_datetime = models.DateTimeField(verbose_name='Create Datetime', auto_now_add=True)

    bucket = models.CharField(verbose_name="Bucket Name for S3", max_length=64, blank=True, null=True)
    S3_key = models.CharField(verbose_name='S3 Key', max_length=64, blank=True, null=True)
    S3_secret_key = models.CharField(verbose_name='S3 Secret Key', max_length=64, blank=True, null=True)


class ProjectUser(models.Model):
    """ participants """

    user = models.ForeignKey(verbose_name='User', to='UserInfo', related_name='projects', on_delete=models.CASCADE)
    invitor = models.ForeignKey(verbose_name='Invitor', to='UserInfo', related_name='invites', null=True, blank=True,
                                on_delete=models.CASCADE)
    project = models.ForeignKey(verbose_name='Task', to='Project', on_delete=models.CASCADE)
    star = models.BooleanField(verbose_name='Star', default=False)
    create_datetime = models.DateTimeField(verbose_name='Joining Time', auto_now_add=True)
