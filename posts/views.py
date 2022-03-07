from django.shortcuts import render
from rest_framework import generics
from posts.serializers import postSerializer
from .models import Post

# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = postSerializer
    
