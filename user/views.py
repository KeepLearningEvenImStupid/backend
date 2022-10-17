from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .serializers import *
from rest_framework import viewsets, permissions, generics
from knox.models import AuthToken
from rest_framework.response import Response
# Create your views here.


class userDataViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer


class groupDataViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = groupSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = userRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": userSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
