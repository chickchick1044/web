from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.index, name='index'), # GET /students/
    path('new/', views.new, name='new'), # GET /students/new/
    # path('create/', views.create, name='create'), => 주소자체에 표현이 들어가서X (자원만 포함해야), 해결: GET과 POST를 합친다
    path('<int:pk>/', views.detail, name='detail'), # GET /students/1/
    path('<int:pk>/edit/', views.edit, name='edit'), # GET, POST /student/1/edit
    # path('<int:pk>/update/', views.update, name='update'), # POST /students/1/update(X)
    path('<int:pk>/delete/', views.delete, name='delete'), # POST /students/1/delete => Restful하진 않지만, 장고는 delete를 지원하지 않음
    path('<int:student_pk>/comments/new/', views.comments_new, name='comments_new'),
    path('<int:student_pk>/comments/<int:pk>/delete', views.comments_delete, name='comments_delete'), # POST /students/1/comments/1/delete
    path('<int:student_pk>/comments/<int:pk>/edit', views.comments_edit, name='comments_edit'),

]

# URL Name
# path('주소/', views.함수, name='이름')
# {% url '이름'%} => /students/이름/가 자동으로 생성
# [장점]
# 1. 주소의 변경이 필요할 때, urls.py에서만 수정해주면 됨
# 2. 마지막 '/'를 빼먹는 실수를 차단할 수 있음

# App Name - 특정 app의 urls.py 자체
# {% url 'app_name:path_name' %}

# RESTful- Rest의 구성요소
# 1. 자원(Resource) - URI: 무엇을 가져올지
# 2. 행위(Verb) - HTTP Method (GET, POST, PUT, DELETE, )
# 3. 표현(Representation) - 자원 + 행위
# ex)
# GET    /users/1 =>user 1번 가져옴
# PUT    /users/1
# DELETE /users/1
