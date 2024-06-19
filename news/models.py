from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=255,null=False)
    imagefile = models.ImageField(upload_to="post_images", default="default_news.jpg")
    description = models.TextField(null=True, blank=True)
    post = models.TextField(null=True, blank=True)
    created_at =  models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title