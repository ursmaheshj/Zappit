from django.shortcuts import render
from rest_framework import generics
from posts.serializers import postSerializer
from .models import Post

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = postSerializer
    
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)