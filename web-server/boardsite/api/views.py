from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# api/views.py
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)