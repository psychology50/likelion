from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='accounts'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
]
