from django.shortcuts import render
from .models import Post

# dummy post data
posts = Post.objects.all()

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})