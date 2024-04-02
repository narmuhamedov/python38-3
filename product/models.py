from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Напишите тег',
                            default='#')

    def __str__(self):
        return f'#{self.name}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
