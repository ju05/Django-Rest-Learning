from rest_framework import serializers
from .models import Post, Author

class PostSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedIdentityField(view_name = 'author')
    class Meta:
        model = Post
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'