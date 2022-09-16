# Generated by Django 4.1.1 on 2022-09-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_project_name_alter_projectuser_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name_space',
            field=models.CharField(default='ggr', max_length=32, verbose_name='Namespace'),
        ),
        migrations.AlterField(
            model_name='project',
            name='S3_key',
            field=models.CharField(blank=True, default='4G8F4PBHBLNX7ZOW8N5P', max_length=64, null=True, verbose_name='S3 Key'),
        ),
        migrations.AlterField(
            model_name='project',
            name='bucket',
            field=models.CharField(blank=True, default='ggr-bucket-cbf77f1e-eea2-4b4a-88b2-ae787daf3f42', max_length=64, null=True, verbose_name='Bucket Name for S3'),
        ),
    ]