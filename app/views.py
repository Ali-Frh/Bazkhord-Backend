from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import UserSerializer

"""
this is the register view, it is used to register new users
"""


class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request) -> Response:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Use username for JWT token generation as it's the standard field
            token_serializer = TokenObtainPairSerializer(
                data={
                    "username": getattr(user, "username"),
                    "password": request.data["password"],
                }
            )
            token_serializer.is_valid(raise_exception=True)
            return Response(
                token_serializer.validated_data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
