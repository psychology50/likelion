"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # include를 import함으로써 url의 반복을 사용하지 않고 관리할 수 있게 만든다

from myapp import views

# 현재 django의 주소 "http://127.0.0.1:8000/"
# 요청 "http://127.0.0.1:8000/1", "http://127.0.0.1:8000/2" 이런 식으로 들어올 경우?

# path('/test', FUNCTION) -> url 뒤에 '/test'가 붙으면 FUNCTION을 실행해라.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # 아무것도 입력 안 한 default
    path('about/', views.about, name='about'),
    path('products/', include('product.urls')),
    path('boards/', include('board.urls')),
]

# 상품 관련 url
  # 127.0.0.1:8000/products/1
  # 127.0.0.1:8000/products/2
  # 127.0.0.1:8000/products/3
# 이럴게 아니라.. python manage.py startapp product 로 앱을 만들고 강제적으로 urls.py를 생성하여 product의 url은 모두 얘네가 담당하게 만든다.

