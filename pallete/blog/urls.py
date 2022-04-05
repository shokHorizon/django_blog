from django import views
from django.urls import path
from . import views

urlpatterns=[
    path('post/<int:pk>/', views.post_view, name='post'),
    path('search_post/', views.search_post, name='search_post'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('edit_post/<int:pk>/', views.UpdatePostView.as_view(), name='edit_post'),
    path('delete_post/<int:pk>/', views.DeletePostView.as_view(), name="delete_post"),
    path('like_post/<int:post_id>/', views.likePostView, name='like_post'),
    path('create_comment/<int:post_id>/', views.create_comment, name='create_comment'),
    path('', views.index, name='index'),
]

