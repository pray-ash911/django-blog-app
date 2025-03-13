from django.http import HttpResponse
from .forms import BlogPostForm
from django.shortcuts import  render,redirect

def home(request):
    return HttpResponse("Welcome to my Blog")

def homes(request):
    return HttpResponse("Hello Blog")


def add_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after submission
    else:
        form = BlogPostForm()

    return render(request, 'add_post.html', {'form': form})