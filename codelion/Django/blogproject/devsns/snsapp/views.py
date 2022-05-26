from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm, PostForm, FreePostForm, FreeCommentForm
from .models import Post, FreePost

# Create your views here.

def home(request):
    #posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

def postCreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})

def new_comment(request, post_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        finished_form = form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
    return redirect('detail', post_id)

def freehome(request):
    #posts = Post.objects.all()
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request, 'free_index.html', {'freeposts':freeposts})

def freedetail(request, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentForm()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

def freepostCreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('freehome')
    else:
        form = FreePostForm()
    return render(request, 'free_post_form.html', {'form':form})

def new_freecomment(request, post_id):
    form = FreeCommentForm(request.POST)
    if form.is_valid():
        finished_form = form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=post_id)
        finished_form.save()
    return redirect('freedetail', post_id)

     