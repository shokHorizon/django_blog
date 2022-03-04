from django import views
from django.urls import path
from . import views

urlpatterns=[
    path('post/<int:pk>/', views.PostView.as_view(), name='post'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('edit_post/<int:pk>/', views.UpdatePostView.as_view(), name='edit_post'),
    path('delete_post/<int:pk>/', views.DeletePostView.as_view(), name="delete_post"),
    path('', views.index, name='index'),
]

