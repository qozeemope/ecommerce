from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(id=response.data["id"])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"user": response.data, "token": token.key})