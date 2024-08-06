from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']


    def save(self, commit=True, user=None):
        article = super().save(commit=False)
        article.author = user  # 현재 사용자로 author 설정
        if commit:
            article.save()
        return article