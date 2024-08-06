from django.contrib import admin
from django.urls import include, path, re_path
from community.views import *


urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 페이지 경로
    path('write/', write, name='write'),  # write 페이지
    path('list/', list, name='list'),  # list 페이지
    path('articles/', include('articles.urls', namespace='articles')),
    re_path(r'^view/(?P<num>[0-9]+)/$', view),  # 정규 표현식으로 view 페이지
    path('', include('community.urls')),  # 기본 경로를 community 앱으로 리디렉션
    path('accounts/', include('accounts.urls')),  # accounts 앱의 URL 포함

]
