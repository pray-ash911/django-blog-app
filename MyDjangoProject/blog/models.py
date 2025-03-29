from sysconfig import get_default_scheme

from django.contrib.auth.management import get_default_username
from django.contrib.auth.models import User
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_username())  # Default user
    image = models.ImageField(upload_to='blog_images/',blank= True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name="comments")
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank=True,null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/',default='default.jpg',blank=True)
    website = models.URLField(blank=True,null=True)
    location = models.CharField(max_length=255, blank=True, null=True)  # ✅ Ensure this field exists

    def __str__(self):
        return self.title
