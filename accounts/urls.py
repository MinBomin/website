# accounts/urls.py
from django.urls import path
from .views import signup, login_view , article_list # login_view는 로그인 뷰의 이름

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),  # 로그인 URL 추가
    path('', article_list, name='article_list'),  # article_list URL 추가
]
