from urllib.request import Request
from django.contrib.auth.models import User, Group
from .serializers import *
from rest_framework import viewsets, permissions, generics
from knox.models import AuthToken
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.http import JsonResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
# Create your views here.


class userDataViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer


class groupDataViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = groupSerializer


class userRegisterAPI(generics.GenericAPIView):
    serializer_class = userRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": userSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class userLogin(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    redirect_authenticated_user = True

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(userLogin, self).post(request, format=None)


class tokenViewSet(generics.ListAPIView):
    queryset = AuthToken.objects.all()
    serializer_class = tokenSerializer
