from django.shortcuts import render, redirect, get_object_or_404
from community.forms import Form
from .models import Article  # 실제 사용하려는 폼의 이름으로 수정
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login as auth_login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse

def write(request):
    if request.method == 'POST':
        form = Form(request.POST)  # POST 요청 시 폼에 데이터 바인딩
        if form.is_valid():
            form.save()  # 데이터 저장
            return redirect('list')  # 성공적으로 처리 후 'list'로 리디렉션
    else:
        form = Form()  # GET 요청 시 폼 인스턴스 생성

    return render(request, 'community/write.html', {'form': form})  # 폼을 템플릿에 전달

def list(request):
    articleList = Article.objects.all()
    return render(request, 'community/list.html', {'articleList': articleList})

def view(request, num):
    article = get_object_or_404(Article, number=num)  # number 필드로 Article 검색
    return render(request, 'community/view.html', {'article': article})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/articles/')  # articles 페이지로 리다이렉트
    else:   
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'community/login.html', context)

def custom_logout(request):
    logout(request)
    return redirect('community:login') 

def home(request):
    return render(request, 'community/home.html')  # home.html 템플릿을 렌더링

def some_view(request):
    form = Form()
    return render(request, 'template_name.html', {'form': form})