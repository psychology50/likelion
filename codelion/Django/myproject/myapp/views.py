from django.shortcuts import render

# Create your views here.
'''
def home(request):
    return render(request, 'index.html') # 요청이 들어올 때 index.html을 렌더링하는 함수
'''

def first(request):
    return render(request, 'first.html')

def second(request):
    return render(request, 'second.html')