# Generated by Django 3.2.6 on 2021-09-05 21:56

import activities.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landinfo',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to=activities.models.save_lesson_files, verbose_name='Land certificate'),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='lga_situated',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='landinfo',
            name='state',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='landinfo',
            name='land_status',
            field=models.CharField(choices=[('RENTAL', 'Rental'), ('AVAILABLE', 'Available'), ('SOLD', 'Sold')], default='AVAILABLE', max_length=30),
        ),
    ]
