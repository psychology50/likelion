'''
1. 김멋사는 lionshop 이라는 온라인 쇼핑몰 프로젝트를 만들려고 한다.  
해당 프로젝트는 `**products**` , `**profile**` 두개의 앱으로 구성되어있고 
products 앱에서는 `**top`,** `**outer`,**  `**pants**` 페이지의 url을,  
profile 앱에서  `**order_list`,** `**point`,** `**cart**`페이지의 url을 관리하고있다.
아래를 참고하여 lionshop, products, profile의 urls.py 파일을 완성하세요

🐘
1️⃣ 각 페이지의 화면을 불러오는 views.py의 함수 이름은 각 페이지의 이름으로 통일한다
2️⃣ 생성되는 페이지의 이름과 url은 다음과 같다 
home →127.0.0.1:8000/
products →127.0.0.1:8000/products/
top →127.0.0.1:8000/products/top/
outer →127.0.0.1:8000/products/outer/
pants →127.0.0.1:8000/products/pants/
profile →127.0.0.1:8000/profile/
order_list →127.0.0.1:8000/profile/order_list/
point →127.0.0.1:8000/profile/point/
cart →127.0.0.1:8000/profile/cart/

<=== ionshop/urls.py ===>
from django.contrib import admin
from django.urls import path, _____

urlpatterns = [
    path('admin/', admin.site.urls),
    _____,
		_____,
		_____,
]

<=== products/urls.py ===>
from django.urls import path
_____

urlpatterns = [
		_____,
		_____,
		_____,
		_____,
]

<=== profile/urls.py ===>
from django.urls import path
_____
urlpatterns = [
		_____,
		_____,
		_____,
		_____,
]
'''

from django.contrib import admin
from django.urls import path, include
from lionshop import views # 이 부분 빠져있었어요

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products', include('products.urls')),
    path('profile/', include('profile.urls')),
]

# <=== products/urls.py ===>
from django.urls import path
from products import views

urlpatterns = [
	path('', views.products),
    path('top/', views.top, name='top'),
    path('outer/', views.outer, name='outer'),
    path('pants/', views.pants, name='pants'),
]

# <=== profile/urls.py ===>
from django.urls import path
from profile import views

urlpatterns = [
	path('', views.products),
    path('order_list/', views.order_list, name='order_list'),
    path('point/', views.point, name='point'),
    path('cart/', views.cart, name='cart'),
]


'''
2. static폴더에 css 폴더안에 있는 style.css 파일을 사용할 수 있도록 빈칸에 알맞은 코드를 작성하여라

html
(1)___________
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
		(2)___________
</head>
<body>
    <div>hello</div>
</body>
</html>

'''

# html
# {% load static %}
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
#     <link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap.css' %}">
# </head>
# <body>
#     <div>hello</div>
# </body>
# </html>


'''
3. about.html 파일은 home.html 파일을 상속한다. 다음 home.html을 참고해 빈칸에 알맞은 코드를 작성하여라 

<=== home.html ===>

<!DOCTYPE html>
<html lang="Ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Document</title>
</head>
<body>
 {% block home %}
 {% endblock %}
    
</body>
</html>

<=== about.html ===>

(1)_______

(2)_______
		<div>about page</div>
(3)_______
'''

# <=== about.html ===>

# {% extends 'home.html' %}

# {% block home %}
# 		<div>about page</div>
# {% endblock %}