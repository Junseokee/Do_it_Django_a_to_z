from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk') #pk를 기준으로 정렬하고 posts로 정의

    return render(
        request,
        'blog/index.html',
        {
            'posts' : posts,
        }
    )