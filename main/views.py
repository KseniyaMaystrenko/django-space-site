from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from django.db import models

from .forms import PoolForm, CommentForm, BlogForm
from .models import Blog, Comment

def home(request):
    return render(request, 'main/home.html', {'title': 'Главная страница'})

def links(request):
    return render(request, 'main/links.html', {'title': 'Полезные ресурсы'})

def pool(request):
    liked_dict = {'1': 'Дизайн', '2': 'Удобство навигации', '3': 'Полезная информация', '4': 'Скорость работы'}
    data = None
    if request.method == 'POST':
        form = PoolForm(request.POST)
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'], 'rate': form.cleaned_data['rate'],
                'liked': liked_dict[form.cleaned_data['liked']], 'wishes': form.cleaned_data['wishes'],
                'subscribe': 'Да' if form.cleaned_data['subscribe'] else 'Нет',
                'email': form.cleaned_data['email'] if form.cleaned_data['email'] else 'Не указан'
            }
            form = None
    else:
        form = PoolForm()
    return render(request, 'main/pool.html', {'form': form, 'data': data})

def registration(request):
    if request.method == "POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            reg_f.save()
            return redirect('home')
    else:
        regform = UserCreationForm()
    return render(request, 'main/registration.html', {'regform': regform, 'year': datetime.now().year})

# --- ФУНКЦИИ ДЛЯ БЛОГА ---

def blog(request):
    """Страница со списком статей"""
    posts = Blog.objects.all().order_by('-posted')
    return render(request, 'main/blog.html', {'title': 'Блог', 'posts': posts})

def blogpost(request, parametr):
    """Страница конкретного поста с комментариями"""
    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = post_1
            comment_f.save()
            return redirect('blogpost', parametr=post_1.id)
    else:
        form = CommentForm()

    return render(request, 'main/blogpost.html', {
        'post_1': post_1,
        'comments': comments,
        'form': form,
        'year': datetime.now().year,
    })

# --- НОВЫЕ ФУНКЦИИ ДЛЯ 9 ЛАБЫ ---

def newpost(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post_f = form.save(commit=False)
            post_f.author = request.user
            post_f.posted = datetime.now()
            post_f.save()
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, 'main/newpost.html', {'form': form, 'title': 'Добавить статью'})

def videopost(request):
    return render(request, 'main/videopost.html', {'title': 'Видео'})