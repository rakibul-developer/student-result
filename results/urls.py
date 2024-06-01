from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_result, name='search_result'),
    path('students/', views.student_list, name='student_list'),
    path('students/new/', views.student_create, name='student_create'),
    path('students/<int:pk>/edit/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
]
