# Generated by Django 3.2.6 on 2021-09-06 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_alter_landinfo_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landinfo',
            name='plot',
            field=models.FloatField(max_length=20),
        ),
        migrations.AlterField(
            model_name='landinfo',
            name='price',
            field=models.FloatField(max_length=20),
        ),
    ]
