from rest_framework import serializers
from .models import Blog, BlogView, Country
from django.contrib.auth.models import User

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'user', 'country', 'created_at']

class BlogViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogView
        fields = ['id', 'blog', 'user', 'country', 'viewed_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
