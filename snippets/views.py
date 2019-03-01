from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics, permissions
from snippets import models
from snippets import serializers



class SnippetList(generics.ListCreateAPIView):

    # lookup_field = 'pk'
    # serializer_class = serializers.SnippetSerializer


    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
