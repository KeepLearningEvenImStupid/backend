from dataclasses import fields
from admission.models import Admission, Angkatan
from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import *


class pertanyaanSerializer(serializers.ModelSerializer):
    class Meta:
        model = pertanyaan
        fields = ['penanya', 'pertanyaan', 'jawaban']


class jawabanSerializer(serializers.ModelSerializer):
    class Meta:
        model = jawabanModels
        fields = ['penjawab', 'jawaban']
