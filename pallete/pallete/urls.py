from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('django.contrib.auth.urls')),
    path('user/', include('user.urls')),
    path('', include('blog.urls')),
]
