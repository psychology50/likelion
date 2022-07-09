from django.urls import path
from .views import ( 
    CustomUserCreate, 
    CustomUserLogin,
    ChangePasswordView,
    CustomUserLogout
)
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('login/', CustomUserLogin.as_view(), name="token_obtain_pair"),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_pw/<int:pk>/', ChangePasswordView.as_view(), name='change_pw'),
    path('logout/', CustomUserLogout.as_view(), name="logout")
]
