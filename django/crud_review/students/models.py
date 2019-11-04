from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField() # default, ~이상 
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

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # CASCADE : 1:N에서 1이 삭제되면 N도 삭제
    # PROTECT : 1을 삭제하려 할 때, N이 있으면 삭제 불가능
    # SET_NULL : 1이 삭제가 되면 N의 컬럼에 NULL로 설정
    # DO_NOTHING : 아무것도 하지 않음

    # 1. 1번 학생(1) 가져오기
    # student = Student.objects.get(pk=1)

    # 2. 댓글(N) 생성
    # comment = Comment()
    # comment.content = 'First Comment'
    # comment.student = student
    # comment.student_id = student.pk
    # comment.save()

    # 3. 댓글(N)로 부터 학생(1) 불러오기
    # comment.student => student 인스턴스 자체
    # comment.student.age => 학생 나이
    # comment.student.name => 학생 이름

    # 4. 학생(1)으로부터 댓글(N) 불러오기
    # student.comment_set.all() => comment QuerySet