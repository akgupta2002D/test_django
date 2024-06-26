

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('todolist/', views.todo_list, name='todo_list'),
    path('', views.base, name='base'),
    path('upload/', views.profile_picture_upload, name='profile_picture_upload'),
]
