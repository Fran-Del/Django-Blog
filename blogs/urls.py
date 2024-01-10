""" define the urls for the blog """

from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Shows all blog post
    path('blogs/', views.post_list, name='post_list'),
    # Shows a single blog post
    path('blogs/<int:post_id>/', views.post, name='post'),
    # Shows about page
    path('about/', views.about, name='about'),
    # Shows contact page
    path('contact/', views.contact, name='contact'),
    # Adds a comment to a post
    #path('add_comment/<int:post_id>/', views.add_comment_to_post, name='add_comment_to_post'),
]