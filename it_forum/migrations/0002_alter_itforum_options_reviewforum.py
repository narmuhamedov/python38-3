# Generated by Django 5.0.3 on 2024-03-22 11:47

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itforum',
            options={'verbose_name': 'вопрос', 'verbose_name_plural': 'вопросы про python'},
        ),
        migrations.CreateModel(
            name='ReviewForum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('stars', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('name_correction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correct', to='it_forum.itforum')),
            ],
        ),
    ]
