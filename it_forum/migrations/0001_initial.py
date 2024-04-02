# Generated by Django 5.0.3 on 2024-03-19 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItForum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Как вас зовут?')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Укажите вашу почту')),
                ('description', models.TextField(verbose_name='Опишите вашу проблему')),
            ],
        ),
    ]
