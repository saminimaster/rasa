from rest_framework import serializers
from rest_framework.response import Response
from .models import Pages, Post, UserModel


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserModel.objects.create_user(validated_data['username'], None,validated_data['password'])
        return user
# User Register
        
class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = ('id', 'page_title')
class PostSerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'post_title', 'pages')
# GET user POSTS and PAGES
#TODO: it ↑↑↑↑ dosen't show the foldering thing

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
#TODO: make it that it select the created post as one of the user's posts Automaticly