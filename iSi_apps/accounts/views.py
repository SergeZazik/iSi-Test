from rest_framework_jwt.views import JSONWebTokenAPIView

from iSi_apps.accounts.serializers import CustomJSONWebTokenSerializer


class CustomObtainJSONWebToken(JSONWebTokenAPIView):
    """
    API View that receives a POST with a user's username and password.
    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = CustomJSONWebTokenSerializer
