from rest_framework import serializers
from .models import Post

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','url','poster','created']
