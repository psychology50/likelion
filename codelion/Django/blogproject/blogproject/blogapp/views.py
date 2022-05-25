from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Blog

def home(request):
    # 블로그 글들을 모조리 띄우는 코드
    # posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('-date') # -붙이면 내림차순
    return render(request, 'index.html', {'posts':posts})

def new(request):
    return render(request, 'new.html')

# === 블로그 글을 저장해주는 함수 ===
from django.utils import timezone

def create(request):
    if request.method == 'POST':
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home') # 특정 html로 다시 재전송해라.

# === django form 사용 ===
from .forms import BlogForm, BlogModelForm, CommentForm

def formcreate(request): # django form을 이용해서 입력받을 경우, 하나의 url에서 GET, POST 모두 처리하게 만들 수 있다.
    # GET : 입력값을 받을 수 있는 HTML을 가져다 줘야 한다.
    # POST : 입력값을 DB에 반영한다.
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'form_create.html', {'form':form}) # render 함수 3번 째 인자 : views.py 내 데이터를 html에 넘길 수 있는데, dict 자료형이어야 한다

# === Model form 사용 ===
def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES) # form 자체적으로 save 메서드를 가지고 있다.
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form':form})


def detail(request, blog_id): # import get_object_or_404
    # blog_id번 째 블로그 글을 DB로부터 들고와서 detail.html로 띄워주는 함수
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    comment_form = CommentForm()


    return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form':comment_form})

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False) # 아직 저장하면 안 된다. 외래키 지정 때문에
        finished_form.post = get_object_or_404(Blog, pk=blog_id) # 외래키값 저장
        finished_form.save()
    return redirect('detail', blog_id)

