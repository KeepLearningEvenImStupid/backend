from django.db import models

from slugify import slugify


class Form(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=255)
    no_hp = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    user_msg = models.CharField(max_length=255)
