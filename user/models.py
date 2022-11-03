from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.contrib.auth.models import *
from django.core.mail import send_mail
# Create your models here.
