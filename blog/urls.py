#created in part2
from django.urls import path
from . import views

urlpatterns = [
    #dont need any path, because this is for all blog sites
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='about'),
]


# <app>/<model>_<viewtype>.html
# 	blog/post_list.html
