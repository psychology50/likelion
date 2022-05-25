'''
[ 과제 설명 - 멋자 지원서 만들기 ] 
여러분은 프론트엔드로부터 완성된 apply.html을 받았습니다….

지원자로부터 이름,학번과 답변을 입력받고, 저장한 후 admin에서 볼 수 있도록 코드를 채워주세요 ( modelform 사용 )

1. 지원서 제출 후에는 home.html화면이 보이도록 해주세요
2. 코드 옆에 주석도 간단하게 달아주세요 🙌
3. ‘코드 작성해주세요’ 적힌 파일만 수정해주세요
4. 빈칸(_______)과, ⭐️부분 모두 코드 작성해주세요
'''

# ========== [ apply.html ] : 5개의 질문 html - 코드 추가 필요없음 ==========
'''
<div class="contactForm">
	<form action="{% url 'create' %}" method="POST">
		<div class="applicant">
			<input type="text" value="이름" name="name"/>
            <input type="text" value="학번" name="id"/>
		</div>

		<h2>가장 자신있는 언어는 무엇인가요?</h2>
		<div class="inputBox">
		    <textarea required="required" name = "answer1"></textarea>
		    <span>답변</span>
		</div>

		<h2>살면서 가장 뿌듯했던 기억은 무엇인가요?</h2>
		<div class="inputBox">
		    <textarea required="required" name = "answer2"></textarea>
		    <span>답변</span>
		</div>

		<h2>가장 열심히 해본 기억이 있다면 어떤 것인가요?</h2>
		<div class="inputBox">
		    <textarea required="required" name = "answer3"></textarea>
		    <span>답변</span>
		</div>

		<h2>멋쟁이사자에서 어떤 것들을 만들어가고 싶나요?</h2>
		<div class="inputBox">
		    <textarea required="required" name = "answer4"></textarea>
		    <span>답변</span>
		</div>

		<h2>멋쟁이사자처럼에 지원하게된 동기가 무엇인가요?</h2>
		<div class="inputBox">
		    <textarea required="required" name = "answer5"></textarea>
		    <span>답변</span>
		</div>
        
		<div class="inputBox">
		    <input type="submit" name="" value="지원하기">
		</div>              
	</form>                    
</div>
'''

# ==========[ models.py ] - 코드 작성해주세요==========
'''
from django.db import models

class Apply(________):
   ⭐️클래스 내용 작성하기⭐️

'''

from django.db import models

class Apply(models.Model):
	name = models.CharField(max_length=50)
	id = models.CharField(max_length=50)
	answer1 = models.TextField()
	answer2 = models.TextField()
	answer3 = models.TextField()
	answer4 = models.TextField()
	answer5 = models.TextField()


# ==========Bash==========
'''
[**TERMINAL]
models.py를 작성한 후, terminal에 입력할 명령어?**
⭐️명령어 작성하기⭐️
'''

# python manage.py makemigrations
# python manage.py migrate


# ==========[ urls. py ] - 코드 추가 필요없음==========
'''
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
	path('admin/', admin.site.urls),
	path('', views.home, name="home"),
	path('apply/', views.apply, name="apply"),
	path('create/', views.create, name="create"),
]
'''

# ==========[  views.py ] - 코드 작성해주세요==========
'''
from django.contrib import auth
from _______ import ________
from _______ import ________

def home(request):
    return render(request, 'home.html')

def apply(request): # 지원서 html
    return render(request, 'apply.html')

def create(request):
    ⭐️메서드 작성하기⭐️

'''

from django.contrib import auth
from django.shortcuts import render, redirect
from .forms import ApplyForm

def home(request):
    return render(request, 'home.html')

def apply(request): # 지원서 html
    return render(request, 'apply.html')

def create(request):
	if request.method == 'POST':
		form = ApplyForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	# GET은 구현하지 않음



# ==========[ forms.py ] - 코드 작성해주세요==========
'''
from dataclasses import field
from django import forms
from ______ import ________

class ApplyForm(___________):
	class Meta:
     ⭐️클래스 내용 작성하기⭐️
'''

from dataclasses import field
from django import forms
from .model import Apply

class ApplyForm(forms.ModelForm):
	class Meta:
		model = Apply
		fields = '__all__'

# ==========[ admin.py ] - 코드 작성해주세요==========
'''
from django.contrib import admin
from _______ import ________

admin.site.register(________)
	
'''

from django.contrib import admin
from .models import Apply

admin.site.register(Apply)