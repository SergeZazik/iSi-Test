from django.shortcuts import render
from rest_framework import viewsets
from iSi_apps.accounts.models import CustomUser
from rest_framework.permissions import IsAuthenticated
from iSi_apps.accounts.serializers import CustomUserSerializer

# Create your views here.


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
