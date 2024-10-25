from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import register, login_view, logout_view, base, home, about

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('base/', base, name='base'),
    path('about/', about, name='about'),
    path('', home, name='home'),
    path('quiz/result/', views.quiz_result_view, name='quiz_result'),
]
