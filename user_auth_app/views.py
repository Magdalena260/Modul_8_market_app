from django.shortcuts import render

from rest_framework import generics
from user_auth_app.models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegistationSerializer
from rest_framework.authoken.models import Token
from rest_framework.response import Response


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistationSerializer(data=request.data)

        if serializer.is_valid():
            saved_account = serializer.save()
            token = Token.objects.get_or_create(user=saved_account)
            data = {
               'token':token.key,
               'username':saved_account.username,
               'email':saved_account.mail

            }
        else:
            data=serializer.errors

            return Response(data)
