from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class jawabanModels(models.Model):
    penjawab = models.ForeignKey(User, on_delete=models.CASCADE)
    jawaban = models.CharField(max_length=255)

    def __str__(self):
        return self.penjawab.username


class pertanyaan(models.Model):
    penanya = models.ForeignKey(User, on_delete=models.CASCADE)
    pertanyaan = models.CharField(max_length=255)
    jawaban = models.ForeignKey(jawabanModels, on_delete=models.CASCADE)

    def __str__(self):
        return self.penanya.username, self.jawabanModels.jawaban
