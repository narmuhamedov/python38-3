from django.db import models


class BlogNews(models.Model):
    TYPE_NEWS_CHOICES = (
        ('Любовь', 'Любовь'),
        ('Шоубизнес', 'Шоубизнес'),
        ('Авто', 'Авто'),
        ('Вечерний Бишкек', 'Вечерний Бишкек')
    )

    title = models.CharField(max_length=100, null=True, verbose_name='Напишите название новости')
    description = models.TextField(null=True, verbose_name='Напишите описание новости')
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Загрузите фото')
    music = models.FileField(upload_to='music/', null=True, blank=True,
                             verbose_name='Загрузите музыкальный файл')
    type_news = models.CharField(max_length=100, choices=TYPE_NEWS_CHOICES, null=True,
                                 verbose_name='Выберите тип новости')
    youtube_url = models.URLField(null=True, verbose_name='Вставьте URL видео с YOUTUBE')
    price = models.PositiveIntegerField(null=True, blank=True, default=100, verbose_name='Укажите цену')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
