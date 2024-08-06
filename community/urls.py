# community/urls.py
from django.urls import path, include
from .views import write, list, view, login, custom_logout, home
from django.contrib import admin

app_name = 'community'

urlpatterns = [
    path('articles/', include('articles.urls')),
    path('', home, name='home'),  # 기본 페이지
    path('list/', list, name='list'),  # list 페이지
    path('write/', write, name='write'),  # write 페이지
    path('view/<int:num>/', view, name='view'),  # 상세보기
    path('login/', login, name='login'),  # 로그인 페이지
    path('logout/', custom_logout, name='logout'),  # 로그아웃 페이지
    path('admin/', admin.site.urls),
]
