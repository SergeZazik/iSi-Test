from rest_framework.routers import DefaultRouter
from iSi_apps.dialogs.views import MessageViewSet, ThreadViewSet


router = DefaultRouter()

router.register(r'threads', ThreadViewSet, 'threads-api')
router.register(r'messages', MessageViewSet, 'messages-api')

urlpatterns = router.urls
