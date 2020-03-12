from django.urls import path, include

from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostView #, Predict

post_list = PostView.as_view({
    'post': 'create',
    'get': 'list'
})
post_detail = PostView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
   # path('predict', Predict.as_view() , name = 'predict'),
]