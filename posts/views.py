from django.shortcuts import render
from rest_framework import generics,permissions
from posts.serializers import postSerializer, voteSerializer
from .models import Post, Vote

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = postSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)

class VoteList(generics.CreateAPIView):
    serializer_class = voteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user,post=post)

    def perform_create(self, serializer):
        serializer.save(voter=self.request.user,post=Post.objects.get(pk=self.kwargs['pk']))