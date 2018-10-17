from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from iSi_apps.accounts.views import CustomUserViewSet


router = DefaultRouter()

router.register(r'users', CustomUserViewSet, 'users-api')

urlpatterns = [
    path('user-auth/', obtain_jwt_token),
]

urlpatterns += router.urls
