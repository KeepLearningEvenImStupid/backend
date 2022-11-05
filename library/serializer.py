from rest_framework import serializers
from .models import *


class libraryVisitorForAdminSerializer(serializers.Serializer):
    class Meta:
        model = visitorModels
        fields = ('id_anggota', 'institusi')


class AnggotaForAdminSerializer(serializers.Serializer):
    class Meta:
        model = visitorModels
        fields = ('id_anggota', 'institusi')


class AnggotaRegisterSerializer(serializers.Serializer):
    class Meta:
        model = anggotaModels
        fields = ('id_anggota', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            anggota = anggotaModels.objects.create_user(
                validated_data['id_anggota'], validated_data['password'])

            return anggota
