from django.db import models
from rest_framework import serializers

from category.models import Category, CategorySerializer
from user.models import User, UserSerializer


class Ad(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Заголовок')
    author_id = models.ForeignKey(User, verbose_name='Автор', related_name='author', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Стоимость')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')
    is_published = models.BooleanField(default=True, verbose_name='Состояние')
    image = models.ImageField(upload_to='post_images', null=True, blank=True, verbose_name='Изображение')
    category_id = models.ForeignKey(Category, verbose_name='Категория', related_name='category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name


class AdSerializer(serializers.ModelSerializer):
    author_id = UserSerializer(read_only=True)
    category_id = CategorySerializer(read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'


