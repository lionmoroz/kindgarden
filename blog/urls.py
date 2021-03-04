from django.urls import path, include

from blog.views import PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
   path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
   path('', PostListView.as_view(), name='post_list'),
]