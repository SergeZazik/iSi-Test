from django.urls import path
from iSi_apps.accounts.views import CustomObtainJSONWebToken


urlpatterns = [
    path('api/token-auth/', CustomObtainJSONWebToken.as_view(), name='obtain-jwt'),
]
