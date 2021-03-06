from rest_framework import serializers
from .models import UserModel
from post.models import Pages, Post

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserModel.objects.create_user(validated_data['username'], None,validated_data['password'])
        return user
# POST: User Register
        
class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = ('id', 'page_title', 'page')
class PostSerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'post_title', 'pages')
# GET: GET user POSTS and PAGES

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
# POST: Create new post

class CreatePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = '__all__'
# POST: Create new page

class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
# PATCH: update post_title

class UpdatePagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = '__all__'
# PATCH: update page

class DeletePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
# DELETE: delete post

class DeletePageSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = '__all__'
# DELETE: delete page

