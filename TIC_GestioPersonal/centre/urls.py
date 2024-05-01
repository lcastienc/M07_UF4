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
    path('students/add_student/', views.add_student, name='add_student'),
    path('students/edit_student/<str:pk>/', views.edit_student, name='edit_student'),
    path('students/delete_student/<str:pk>/', views.delete_student, name='delete_student'),
    path('teachers/add_teacher/', views.add_teacher, name='add_teacher'),
    path('teachers/edit_teacher/<str:pk>/', views.edit_teacher, name='edit_teacher'),
    path('teachers/delete_teacher/<str:pk>/', views.delete_teacher, name='delete_teacher'),
]