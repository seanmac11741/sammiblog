from django.shortcuts import render

posts = [
    {
    'author': 'Sean',
    'title': 'Blog Post 1',
    'content': 'first post content',
    'date_posted': 'August 23'
    },
    {
    'author': 'Sean2',
    'title': 'Blog Post 2',
    'content': '2 post content',
    'date_posted': 'August 20'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context) #3rd param is passed to the template and the template can access it
    # return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
