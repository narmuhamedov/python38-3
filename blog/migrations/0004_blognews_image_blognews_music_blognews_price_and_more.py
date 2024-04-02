# Generated by Django 5.0.3 on 2024-03-12 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blognews_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='blognews',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Загрузите фото'),
        ),
        migrations.AddField(
            model_name='blognews',
            name='music',
            field=models.FileField(blank=True, null=True, upload_to='music/', verbose_name='Загрузите музыкальный файл'),
        ),
        migrations.AddField(
            model_name='blognews',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=100, null=True, verbose_name='Укажите цену'),
        ),
        migrations.AddField(
            model_name='blognews',
            name='type_news',
            field=models.CharField(choices=[('Любовь', 'Любовь'), ('Шоубизнес', 'Шоубизнес'), ('Авто', 'Авто'), ('Вечерний Бишкек', 'Вечерний Бишкек')], max_length=100, null=True, verbose_name='Выберите тип новости'),
        ),
        migrations.AddField(
            model_name='blognews',
            name='youtube_url',
            field=models.URLField(null=True, verbose_name='Вставьте URL видео с YOUTUBE'),
        ),
        migrations.AlterField(
            model_name='blognews',
            name='description',
            field=models.TextField(null=True, verbose_name='Напишите описание новости'),
        ),
        migrations.AlterField(
            model_name='blognews',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='Напишите название новости'),
        ),
    ]
