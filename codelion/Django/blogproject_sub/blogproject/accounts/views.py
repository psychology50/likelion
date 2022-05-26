from django.shortcuts import render, redirect

# Create your views here.

from django.contrib import auth # 기존에 있는 회원인지 아닌지, 로그아웃 등의 기능 지원
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST': # POST : 로그인 처리
        userid = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pw) # 이미 저장된 회원이면, 그 유저 객체를 반환한다. 없다면 None
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

    else: # GET : login.html을 띄워줌
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')