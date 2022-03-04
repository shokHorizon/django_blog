from tabnanny import verbose
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.text


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=80)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk})
    

