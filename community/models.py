from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model): 
    name = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField(null = True)
    cdate = models.DateTimeField(auto_now_add = True)
    number = models.IntegerField(default = 0)
    content = models.TextField()  # 이 필드가 있어야 함
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_articles')
    def __str__(self):
        return self.title
    
