from django.urls import path
from .import views

urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('todolist/', views.todo_list, name='todo_list')
]
