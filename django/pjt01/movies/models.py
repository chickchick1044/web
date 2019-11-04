from django.db import models
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50) # 영화명
    title_en = models.CharField(max_length=50, blank=True) # 영화명(영문)
    audience = models.IntegerField(default=0) # 누적 관객수
    open_date = models.DateField(default=timezone.now) # 개봉일
    genre = models.CharField(max_length=50, blank=True) # 장르
    watch_grade = models.CharField(max_length=50, blank=True) # 관람등급
    score = models.FloatField(default=0) # 평점
    poster_url = models.TextField(null=True, blank=True) # 포스터 이미지 URL
    description = models.TextField(null=True, blank=True) # 영화 소개

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'제목:{self.title}, 평점:{self.score}'