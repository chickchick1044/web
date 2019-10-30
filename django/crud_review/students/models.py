from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째 학생 {self.age}살 {self.name}입니다.'
        
# python manage.py makemigrations >> models.py에 생성한 모델을 migrations파일에
# python manage.py migrate >>migrations폴더에 새로 생긴 파일을 DB에 적용

# python manage.py shell >> 파이썬 터미널(장고의 설정들이 들어있는 터미널)
# from articles.models import Article
# article = Article()
# article.title = ''
# article.content = ''
# article.save()