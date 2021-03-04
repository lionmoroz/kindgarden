import random
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    queryset = Post.objects.order_by('-date_created')
    context_object_name = 'posts'
    paginate_by = 6

    


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_post'] = random.sample(list(Post.objects.all()), 3)
        return context





