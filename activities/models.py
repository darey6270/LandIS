from django.db import models
import os
from django.contrib.auth.models import User


def save_subject_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.id:
        filename = 'LandInfo_Pictures/{}.{}'.format(instance.owner, ext)
    return os.path.join(upload_to, filename)


def save_lesson_files(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.id:
        filename = 'certificate_files/{}/{}.{}'.format(instance.owner, instance.owner, ext)
        if os.path.exists(filename):
            new_name = str(instance.id) + str('1')
            filename = 'lesson_images/{}/{}.{}'.format(instance.owner, new_name, ext)
    return os.path.join(upload_to, filename)


# Create your models here.
class LandInfo(models.Model):
    RENTAL = "RENTAL"
    AVAILABLE = "AVAILABLE"
    SOLD = "SOLD"

    STATUS = (
        (RENTAL, 'Rental'),
        (AVAILABLE, 'Available'),
        (SOLD, 'Sold'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='land_user')
    land_status = models.CharField(max_length=30, choices=STATUS, default=AVAILABLE)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    land_size = models.CharField(max_length=150)
    price = models.FloatField(max_length=20)
    plot = models.FloatField(max_length=20)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to=save_subject_image, verbose_name='Land Picture')
    lga_situated = models.CharField(max_length=400, null=True, blank=True)
    state = models.CharField(max_length=400, null=True, blank=True)
    certificate = models.ImageField(upload_to=save_subject_image, verbose_name="Land certificate", null=True, blank=True)

    def __str__(self):
        return self.email
