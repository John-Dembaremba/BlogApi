from rest_framework import generics

from .models import Post
from .serializers import PostSerializers
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostList(generics.ListAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializers

