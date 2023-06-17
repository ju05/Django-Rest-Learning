from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import mixins
from rest_framework.permissions import (IsAdminUser, IsAuthenticated, AllowAny)
from .models import Post, Author
from .serializers import PostSerializer, AuthorSerializer
from .permissions import isManager, isStudent

# CRUD = Create, retrieve, update, delete/destroy

class PostListView(ListAPIView, mixins.CreateModelMixin):
    serializer_class = PostSerializer
    permission_classes = (isManager,)
    def get_queryset(self):
        post_title = self.request.query_params.get('title', None)
        if post_title is not None:
            queryset = Post.objects.filter(title = post_title)
        else: queryset = Post.objects.all()
        return queryset
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostDetailView(RetrieveAPIView):
    permission_classes = (isStudent, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AuthorView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
# ----------------------------------GenericAPIView + Mixins-----------------------------------------------------------

# class PostMixingView(mixins.CreateModelMixin, mixins.ListModelMixin, GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs) # This .list method is a feature from mixins.ListModelMixin
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs) # This .create method is a feature from mixins.CreateModelMixin

# -------------------------------------------APIView-----------------------------------------------
# class PostView(APIView):
#     def get(self, request, *args, **kwargs):
#         if 'pk' in kwargs:
#             post = Post.objects.get(id = kwargs['pk'])
#             serializer = PostSerializer(post)
#             return Response(serializer.data)
#         else:
#             queryset = Post.objects.all()
#             serializer = PostSerializer(queryset, many = True)
#             return Response(serializer.data)
        
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(data = serializer.data)
#         else: return Response(serializer.errors)

#     def delete(self, request, pk, *args, **kwargs):
#         post = Post.objects.get(id = pk)
#         post.delete()
#         return Response()

#     def put(self, request, pk, *args, **kwargs):
#         post = Post.objects.get(id = pk)
#         serializer = PostSerializer(post, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else: return Response(serializer.errors)
