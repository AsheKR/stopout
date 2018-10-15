from django.urls import path

from school import views

urlpatterns = [
    path('', views.school_list, name='school_list'),
    path('school/<int:pk>/', views.school_detail, name='school_detail'),
    path('student_list/', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
]
