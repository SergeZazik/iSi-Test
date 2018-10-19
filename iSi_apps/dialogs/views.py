from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from iSi_apps.permissions import SaveMethodsAdminPermission
from iSi_apps.dialogs.models import Message, Thread
from iSi_apps.dialogs.serializers import MessageSerializer, ThreadSerializer

# Create your views here.


class ThreadViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, SaveMethodsAdminPermission)
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('participant__id',)


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('thread__id',)
