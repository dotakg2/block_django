from django.urls import path 
from .views import *

urlpatterns = [
    path('', categories_list, name='home-page'),
    path('posts/', post_list, name='posts-list'),
    path('posts/<int:pk>', post_detail, name='post-detail')

]