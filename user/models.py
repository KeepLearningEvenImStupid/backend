from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.contrib.auth.models import *
from django.core.mail import send_mail
# Create your models here.


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    send_mail(
        "Password Reset for Iblam",
        'Sorry for interupting you :(,here your password change link : ',
        "iblam@gmail.com",
        [reset_password_token.user.email]
    )
