from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null = True)  # 기본값 추가

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.email and self.author:
            print(f"Setting email from author: {self.author.email}")  # 디버깅 출력
            self.email = self.author.email  # 작성자의 이메일로 설정
        super().save(*args, **kwargs)

    def email(self):
        return self.author.email  # 작성자의 이메일 반환
    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])  # 'article-detail'은 해당 상세 페이지의 URL 이름
    
