from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from django.contrib.auth.models import User

class CustomTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            user = User.objects.get(auth_token__key=key)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        return (user, None)