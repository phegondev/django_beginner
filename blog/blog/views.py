from django.shortcuts import render
from posts.models import Post

def home_page(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'post_list.html', {'posts':posts})

def about_page(request):
    return render(request, 'about.html')
