# Generated by Django 4.1.1 on 2022-09-13 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Project Name')),
                ('color', models.SmallIntegerField(choices=[(1, '#56b8eb'), (2, '#f28033'), (3, '#ebc656'), (4, '#a2d148'), (5, '#20BFA4'), (6, '#7461c2'), (7, '#20bfa3')], default=1, verbose_name='Color')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('use_space', models.IntegerField(default=0, verbose_name='Space used')),
                ('star', models.BooleanField(default=False, verbose_name='Star')),
                ('join_count', models.SmallIntegerField(default=1, verbose_name='Number of participants')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Create Datetime')),
                ('bucket', models.CharField(blank=True, max_length=64, null=True, verbose_name='Bucket Name for S3')),
                ('S3_key', models.CharField(blank=True, max_length=64, null=True, verbose_name='S3 Key')),
                ('S3_secret_key', models.CharField(blank=True, max_length=64, null=True, verbose_name='S3 Secret Key')),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='mobile_phone',
            field=models.CharField(max_length=12, verbose_name='Mobil phone'),
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.BooleanField(default=False, verbose_name='Star')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Joining Time')),
                ('invitor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='web.userinfo', verbose_name='Invitor')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.project', verbose_name='Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='web.userinfo', verbose_name='User')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.userinfo', verbose_name='Creator'),
        ),
    ]
