#created in part2
from django.urls import path
from . import views #this imports something from current directory, that is views.py that we just made


urlpatterns = [
    #dont need any path, because this is for all blog sites
    path('', views.home, name='blog-home'), #sends it to views.home where views is the thing we imported
    # path('', PostListView.as_view(), name='blog-home')
]


# <app>/<model>_<viewtype>.html
# 	blog/post_list.html
