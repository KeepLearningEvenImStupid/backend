from django.contrib.auth.models import User, Group
from .serializers import *
from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import *
from knox.models import AuthToken
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.core.mail import send_mail
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
# Create your views here.


class userDetail(generics.ListAPIView):
    serializer_class = userDetailSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return User.objects.filter(username=username)


class groupDataViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = groupSerializer


class userRegisterAPI(generics.GenericAPIView):
    serializer_class = userRegisterSerializer
    permission_classes = [AllowAny]

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
    permission_classes = [IsAuthenticated, IsAdminUser]


class CustomPasswordResetView:
    @receiver(reset_password_token_created)
    def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

        email_plaintext_message = "https://a7f2-2001-448a-302f-1eed-b89b-46fe-c5dd-b6a4.ngrok.io/password-reset/confirm/?token={}".format(
            reset_password_token.key)

        send_mail(
            "Iblam",
            email_plaintext_message,
            "Iblamuniversity@gmail.com",
            [reset_password_token.user.email],
            fail_silently=False,
        )
