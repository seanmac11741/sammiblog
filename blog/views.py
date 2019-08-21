from django.shortcuts import render

# Create your views here.
def home(request):
    # context = {
    #     'posts': Post.objects.all()
    # }
    # return render(request, 'blog/home.html', context) #3rd param is passed to the template and the template can access it
    return render(request, 'blog/home.html')
