from django.shortcuts import render, redirect
from .models import Post
from django.shortcuts import get_object_or_404, render
from .forms import CreatePost
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'post_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post':post})

@login_required(login_url='/users/login')
def post_add(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
        
    else:
        form = CreatePost()
    return render(request, 'add_post.html', {'form':form})
