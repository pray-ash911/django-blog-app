from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, ListView
from pyexpat.errors import messages

from .forms import BlogPostForm, ProfileForm, UserRegisterForm
from django.shortcuts import render, redirect, get_object_or_404

from .models import BlogPost

def home(request):
    posts = BlogPost.objects.all()
    return render(request,'home.html',{'posts':posts})

def add_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after submission
    else:
        form = BlogPostForm()

    return render(request, 'add_post.html', {'form': form})


def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == "POST":
        form = BlogPostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after saving
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'blog_edit.html', {'form': form, 'post': post})



def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'blog_delete.html', {'post': post})

from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment
from .forms import CommentForm

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)  # Refresh page after comment
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})

@login_required  # Ensures only logged-in users access the profile page
def profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = ProfileForm(instance=profile)

        return render(request,'profile.html',{'form':form,'profile':profile})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect("login")  # Redirect to login page
    else:
        form = UserRegisterForm()
    return render(request, "blog/register.html", {"form": form})