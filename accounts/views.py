# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.template import engines
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    # 템플릿 경로 출력
    try:
        print(engines['django'].get_template('community/signup.html'))
    except Exception as e:
        print("템플릿 로드 실패:", e)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # 비밀번호 해싱
            user.save()
            login(request, user)  # 자동 로그인
            return redirect('articles:article_list')  # 회원가입 후 이동할 페이지
    else:
        form = SignUpForm()
    return render(request, 'community/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('articles:article_list')  # 로그인 후 이동할 페이지
    else:
        form = AuthenticationForm()
    return render(request, 'community/login.html', {'form': form})


def article_list(request):
    # 여기에 로직 추가
    return render(request, 'accounts/article_list.html') 