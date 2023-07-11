from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.migrations import serializer
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import UserSerializer, PostSerializer, UserLoginSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(APIView):
    def post(self, request):
        if request.user.is_autenticated:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(data={'error:invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)
        return Response(status=status.HTTP_200_OK)


class UserLogoutView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)

        return Response({'message': 'Logout successful'})

    serializer_class = UserSerializer


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Post.objects.filter(author=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
