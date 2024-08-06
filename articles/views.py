from django.shortcuts import render, redirect
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm  # ArticleForm을 import 해야 함
from .models import Article  # Article 모델을 import 해야 함
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Article
from django.views.generic import DetailView

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'articles/article_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # 현재 사용자로 작성자 설정
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('articles:article-detail', kwargs={'pk': self.object.pk})  # 작성한 글의 상세 페이지로 리디렉션

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'  # 템플릿 파일
    context_object_name = 'articles'  # 템플릿에서 사용할 컨텍스트 변수
    
    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)  # 작성자가 현재 사용자일 경우

@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()  # 저장
            return redirect('articles:articles_index')  # 올바른 URL 이름 사용
    else:
        form = ArticleForm()  # GET 요청 시 빈 폼 생성

    return render(request, 'articles/add_article.html', {'form': form})

def articles_index(request):
    articles = Article.objects.all()  # 모든 기사를 가져옴
    return render(request, 'articles/index.html')

def my_articles(request):
    if not request.user.is_authenticated:
        return redirect('login')  # 로그인하지 않은 경우 로그인 페이지로 리다이렉트

    articles = Article.objects.filter(author=request.user)  # 현재 사용자가 작성한 기사만 가져옵니다.
    return render(request, 'articles/my_articles.html', {'articles': articles})

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'articles/article_detail.html', {'article': article})



def article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user

        if title and content:
            article = Article(title=title, content=content, author=author)
            article.save()
            return redirect('article_list')  # 목록 페이지로 리디렉션

    return render(request, 'articles/article_form.html')


# 예제: articles/views.py
def article_list(request):
    articles = Article.objects.all()  # 모든 기사 가져오기
    return render(request, 'articles/article_list.html', {'articles': articles})

# 예제: articles/views.py
def my_articles(request):
    if request.user.is_authenticated:
        articles = Article.objects.filter(author=request.user)  # 현재 사용자가 작성한 기사만 가져오기
    else:
        articles = []  # 로그인하지 않은 경우 빈 리스트

    return render(request, 'articles/my_articles.html', {'articles': articles})

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False, user=request.user)  # 현재 사용자 설정
            article.save()
            return redirect('articles:my_articles')  # 내가 쓴 기사 목록으로 리다이렉트
    else:
        form = ArticleForm()
    
    return render(request, 'articles/create_article.html', {'form': form})