from rest_framework import viewsets
from iSi_apps.accounts.models import CustomUser
from iSi_apps.accounts.serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny

# Create your views here.


class CustomUserViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
