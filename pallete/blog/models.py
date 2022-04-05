from tabnanny import verbose
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=15)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=80)
    text = RichTextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, related_name='comments')
    
    def __str__(self) -> str:
        return self.text
