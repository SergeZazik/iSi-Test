from django.urls import path
from iSi_apps.dialogs.views import (MessageCreateAPIView, MessageListAPIView, ThreadCreateAPIView, ThreadListAPIView,
                                    ThreadUpdateAPIView)


urlpatterns = [
    path('api/dialogs/thread/create/', ThreadCreateAPIView.as_view(), name='create_thread'),
    path('api/dialogs/thread/update/<int:pk>', ThreadUpdateAPIView.as_view(), name='update_thread'),
    path('api/dialogs/thread/list/', ThreadListAPIView.as_view(), name='list_threads'),
    path('api/dialogs/message/create/', MessageCreateAPIView.as_view(), name='create_message'),
    path('api/dialogs/message/list/<int:thread>', MessageListAPIView.as_view(), name='list_messages'),
]
