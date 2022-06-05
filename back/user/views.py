from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserRegisterSerializer, PostSerializer, CreatePostSerializer, CreatePageSerializer, UpdatePostTitleSerializer
from .models import UserModel
from post.models import Post, Pages
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegisterView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer
    queryset = UserModel.objects.all()
#TODO: make it so that noone could sighup with ... username or something
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }) 
# user will get a token after registering

class GetUserPostsVIew(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# GET user POSTS and PAGES

class CreatePostView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreatePostSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            data=request.data
            post_title = data['post_title']
            user = self.request.user
            post = Post.objects.create(post_title = post_title)
            user.posts.add(post.id)
            return Response({'SUCCESS:': str(post_title)})
        except Exception as e:
            return Response({'ERROR:': str(e)})
# Create new Post

class CreatePageView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreatePageSerializer

    def create(self, request, *args, **kwargs):
        try:
            data=request.data
            page_title = data['page_title']
            text = data['text']
            post_id = data['post']
            page_id = data['page']
            if page_id != 0:# is there a better way to do this? it check if a page should be under other pages
                page = Pages.objects.get(id = page_id)
                post = Post.objects.get(id = post_id)
                page = Pages.objects.create(page_title = page_title, text = text, post = post, page = page)
                return Response({'SUCCESS:': str(page)})
            else:
                post = Post.objects.get(id = post_id)
                page = Pages.objects.create(page_title = page_title, text = text, post = post)
                return Response({'SUCCESS:': str(page)})

        except Exception as e:
            return Response({'ERROR:': str(e)})
# Create new Page

class UpdatePostTitle(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdatePostTitleSerializer
    queryset = Post.objects.all()

    def update(self, request, *args, **kwargs):
        try:
            user = self.request.user
            data = request.data
            post_id = data['id']
            post_title = data['post_title']
            post = user.posts.get(id=post_id)
            user.posts.update(post_title=post_title)
            return Response({'SUCCESS:': str(post_title)})
        except Exception as e:
            return Response({'ERROR:': str(e)})