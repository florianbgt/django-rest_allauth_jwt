from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import ProfileSerializer, ChangePasswordSerializer

CustomUser = get_user_model()

class Profile(generics.RetrieveUpdateAPIView):
    queryset = CustomUser
    serializer_class = ProfileSerializer
    def get_object(self):
        return self.request.user

class ChangePassword(generics.UpdateAPIView):
    queryset = CustomUser
    serializer_class = ChangePasswordSerializer
    def get_object(self):
        return self.request.user
