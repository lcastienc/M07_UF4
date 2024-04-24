from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_one,name='index_one'),
    path('index/', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('teachers/', views.teachers, name='teachers'),
    path('students/', views.students, name='students'),
    path('students/student/<str:pk>', views.student, name='student'),
    path('teachers/teacher/<str:pk>/', views.teacher, name='teacher'),

]