from django.contrib.auth.models import User, Group
from rest_framework import serializers
from knox.models import AuthToken
from django.contrib.auth import authenticate

from admission.models import Admission


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

# SERIALIZER UNTUK REGISTER USER


class userRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])
        group = Group.objects.get(name='User')
        group.user_set.add(user)
        return user


# GROUP SERIALIZER

class groupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class tokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthToken
        fields = ('user_id', 'token_key')
