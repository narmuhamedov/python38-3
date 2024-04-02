from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ItForum(models.Model):
    name = models.CharField(max_length=100, verbose_name='Как вас зовут?')
    email = models.EmailField(verbose_name='Укажите вашу почту', blank=True)
    description = models.TextField(verbose_name='Опишите вашу проблему')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы про python'


class ReviewForum(models.Model):
    name_correction = models.ForeignKey(ItForum, on_delete=models.CASCADE, related_name="correct")
    text = models.TextField()
    stars = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.text
