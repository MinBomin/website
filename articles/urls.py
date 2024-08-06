# articles/urls.py
from django.urls import path
from .views import ArticleDetailView, ArticleListView, ArticleCreateView, articles_index, add_article, my_articles, article_detail, article_create, article_list

app_name = 'articles'  # 네임스페이스 설정

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),  # 기사 목록 페이지
    path('create/', ArticleCreateView.as_view(), name='article-create'),  # 기사 생성
    path('index/', articles_index, name='articles_index'),  # 인덱스 페이지
    path('add/', add_article, name='add_article'),  # 새 기사 추가
    path('my/', my_articles, name='my_articles'),  # 내가 쓴 기사 목록
    path('detail/<int:article_id>/', article_detail, name='article_detail'),  # 상세 보기 URL
    path('create/', article_create, name='article-create'),  # 기사 생성 추가
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),  # 이 부분이 필요합니다
    path('', article_list, name='article_list'),  # article_list URL 추가
]

