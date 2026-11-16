from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="Заголовок")
    short_description = models.CharField(max_length=255, verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default=datetime.now, db_index=True, verbose_name="Опубликована")
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Автор")
    
    # НОВОЕ ПОЛЕ ДЛЯ КАРТИНКИ (9 лаба)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name="Картинка")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost', kwargs={'parametr': str(self.id)})

# --- НОВАЯ МОДЕЛЬ ДЛЯ КОММЕНТАРИЕВ (Задание 2) ---
class Comment(models.Model):
    text = models.TextField(verbose_name="Текст комментария")
    date = models.DateTimeField(default=datetime.now, verbose_name="Дата добавления")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Статья")

    def __str__(self):
        return f"Комментарий от {self.author} к {self.post}"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date'] # Сортировка: новые сверху

# Регистрируем модели в админке
admin.site.register(Blog)
admin.site.register(Comment)