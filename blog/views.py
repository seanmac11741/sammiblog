from django.shortcuts import render
from .models import Post

posts = [
    {
    'author': 'Sean',
    'title': 'Blog Post 1',
    'content': 'first post content',
    'date_posted': 'August 23',
    'imgurl':'https://i.imgur.com/fnWF6DE.jpg'
    },
    {
    'author': 'Sean2',
    'title': 'Blog Post 2',
    'content': '2 post content',
    'date_posted': 'August 20',
    'imgurl':'https://i.imgur.com/fnWF6DE.jpg'
    }
]

# Create your views here.
def home(request):
    # context = {
    #     'posts': posts
    # }

    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) #3rd param is passed to the template and the template can access it
    # return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
