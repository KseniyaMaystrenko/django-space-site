from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('links/', views.links, name='links'),
    path('pool/', views.pool, name='pool'),
    path('registration/', views.registration, name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    # Маршруты для блога
    path('blog/', views.blog, name='blog'),
    path('blog/<int:parametr>/', views.blogpost, name='blogpost'), # <parametr> - ID статьи
    
    # НОВЫЕ МАРШРУТЫ (9 лаба)
    path('newpost/', views.newpost, name='newpost'),
    path('videopost/', views.videopost, name='videopost'),
]