from rest_framework import serializers
from questionandanswer.models import *


class PertanyaanSerializer(serializers.ModelSerializer):
    class Meta:
        model = pertanyaanDanJawabanModels
        fields = ['penanya', 'pertanyaan']


class JawabanSerializer(serializers.ModelSerializer):
    class Meta:
        model = pertanyaanDanJawabanModels
        fields = ['penanya',
                  'pertanyaan', 'jawaban', 'penjawab']


class PertanyaanJawabanSerializer(serializers.ModelSerializer):
    class Meta:
        model = pertanyaanDanJawabanModels
        fields = ['penanya',
                  'pertanyaan', 'jawaban', 'penjawab', 'slug']
