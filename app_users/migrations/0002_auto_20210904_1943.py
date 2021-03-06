# Generated by Django 3.2.6 on 2021-09-04 18:43

import app_users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user_type',
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=app_users.models.path_and_rename, verbose_name='Profile Picture'),
        ),
    ]
