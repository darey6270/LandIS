# Generated by Django 3.2.6 on 2021-09-03 19:06

import activities.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LandInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_status', models.CharField(choices=[('RESALE', 'Resale'), ('AVAILABLE', 'Available'), ('SOLD', 'Sold')], default='AVAILABLE', max_length=30)),
                ('email', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('land_size', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('plot', models.FloatField(max_length=10)),
                ('location', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=activities.models.save_subject_image, verbose_name='Land Picture')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='land_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]