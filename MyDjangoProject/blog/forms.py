from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import BlogPost, Comment, Profile


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','content','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio','website','location']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
