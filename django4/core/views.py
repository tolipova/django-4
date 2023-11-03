from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
def home(request):
    post = Post.objects.all()
    context = {
        'post':post,

    }
    return render(request, 'index.html' ,context)

def show_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context ={
        'post':post
    }

    return render(request, 'post.html', context)