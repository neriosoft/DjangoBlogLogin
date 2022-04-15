from django.shortcuts import render

# dummy post data
posts = [
    {
        'author': 'Neriosoft',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'January 15, 2022'
    },
    {
        'author': 'Teymebeauty',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'January 16, 2022'
    },
    {
        'author': 'Oreofe',
        'title': 'Blog Post 3',
        'content': 'Third Post Content',
        'date_posted': 'January 18, 2022'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})