from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/token',
        '/token/refresh',
    ]
    return Response(routes)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    def handle_exception(self, exc):
        if isinstance(exc, AuthenticationFailed):
            response = {
                'error': 'Niepoprawne dane logowania. Spróbuj ponownie.'
            }
            return JsonResponse(response, status=status.HTTP_401_UNAUTHORIZED)

        return super().handle_exception(exc)

    serializer_class = MyTokenObtainPairSerializer
