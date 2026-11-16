from django import forms
from .models import Comment, Blog

class PoolForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    rate = forms.ChoiceField(
        label='Оцените сайт по 5-балльной шкале',
        choices=[('5', '5 - Отлично'), ('4', '4 - Хорошо'), ('3', '3 - Удовлетворительно'), ('2', '2 - Плохо'), ('1', '1 - Ужасно')],
        widget=forms.RadioSelect, initial='5'
    )
    liked = forms.ChoiceField(
        label='Что вам понравилось больше всего?',
        choices=(('1', 'Дизайн'), ('2', 'Удобство навигации'), ('3', 'Полезная информация'), ('4', 'Скорость работы')),
        initial='1'
    )
    wishes = forms.CharField(
        label='Ваши пожелания и предложения',
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40})
    )
    subscribe = forms.BooleanField(
        label='Я хочу получать новости сайта на e-mail', required=False
    )
    email = forms.EmailField(label='Ваш e-mail (необязательно)', required=False)

# --- НОВАЯ ФОРМА ДЛЯ КОММЕНТАРИЯ ---
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}

# --- НОВАЯ ФОРМА ДЛЯ СТАТЬИ (9 лаба) ---
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'short_description', 'content', 'image')
        labels = {
            'title': 'Заголовок',
            'short_description': 'Краткое содержание',
            'content': 'Полное содержание',
            'image': 'Картинка',
        }