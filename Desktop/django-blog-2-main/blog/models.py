from django.db import models
from django.contrib.auth.models import User

# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

# Модель поста
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True)  # связь с категориями
    created_at = models.DateTimeField(auto_now_add=True)        # дата создания

    def __str__(self):
        return self.title
