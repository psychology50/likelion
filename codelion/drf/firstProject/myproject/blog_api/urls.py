from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog_api'

urlpatterns = [
    # 세부 정보 생성. DB 개별 구성요소또는 개체 표시
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    # 본직적으로 여기가 홈페이지가 된다. DB의 모든 데이터를 표시
    path('', PostList.as_view(), name='listcreate'),
    
]
