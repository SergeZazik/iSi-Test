from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import (CreateAPIView, ListAPIView, UpdateAPIView, get_object_or_404)
from iSi_apps.accounts.models import UserTypes
from iSi_apps.dialogs.models import Message, Thread
from iSi_apps.dialogs.serializers import MessageSerializer, ThreadSerializer

# Create your views here.


class ThreadCreateAPIView(CreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.user_type != UserTypes.ADMIN.value:
            raise PermissionDenied('Only admin can create new thread')

        return super(ThreadCreateAPIView, self).post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        participants = request.data.get('participants')
        if participants and not request.user.pk in participants:
            request.data['participants'].append(request.user.pk)

        return super(ThreadCreateAPIView, self).create(request, *args, **kwargs)


class ThreadUpdateAPIView(UpdateAPIView):
    serializer_class = ThreadSerializer

    def put(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.user_type != UserTypes.ADMIN.value:
            raise PermissionDenied('Only admin can update thread')

        return super(ThreadUpdateAPIView, self).put(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.threads


class ThreadListAPIView(ListAPIView):
    serializer_class = ThreadSerializer

    def get_queryset(self):
        return self.request.user.threads


class MessageCreateAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageListAPIView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        thread = get_object_or_404(self.request.user.threads, pk=self.kwargs['thread'])
        return thread.messages
