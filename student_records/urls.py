from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_student, name='add_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
]
