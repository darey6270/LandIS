# Generated by Django 3.2.6 on 2021-09-05 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20210905_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landinfo',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
    ]
