from rest_framework.decorators import api_view, permission_classes, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def user_profile(request, tar_username):
    user = get_object_or_404(User, username=tar_username)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)