from rest_framework import serializers
from questionandanswer.models import *


class PertanyaanSerializer(serializers.ModelSerializer):
    class Meta:
        model = pertanyaanDanJawabanModels
        fields = ['penanya', 'pertanyaan', 'email',
                  'nama', 'no_hp', 'judul_pertanyaan', 'dibuat_pada']


class JawabanSerializer(serializers.ModelSerializer):
    class Meta:
        model = pertanyaanDanJawabanModels
        fields = ['penanya',
                  'pertanyaan', 'jawaban', 'penjawab', 'dijawab_pada']


class PertanyaanJawabanSerializer(serializers.ModelSerializer):
    class Meta:
        model = pertanyaanDanJawabanModels
        fields = ['penanya',
                  'pertanyaan', 'jawaban', 'penjawab', 'slug']
