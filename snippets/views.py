from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly



# Create your views here.
class SnippetList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# USER READ ONLY VIEWS

class UserList(generics.ListAPIView):

    queryset = Snippet.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):

    queryset = Snippet.objects.all()
    serializer_class = UserSerializer