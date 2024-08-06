from django.forms import ModelForm 
from community.models import * 
from django import forms
from .models import Article

class Form(ModelForm): 
    class Meta: 
        model = Article 
        fields = ['name','title','contents','url','email','number']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']