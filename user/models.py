from django.db import models
from rest_framework import serializers

from location.models import Location, LocationSerializer


class User(models.Model):
    ROLES = [
        ('member', 'Пользователь'),
        ('admin', 'Администратор'),
        ('moderator', 'Модератор'),
    ]

    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='Фамилия')
    username = models.CharField(max_length=30, db_index=True, verbose_name='Логин', unique=True)
    password = models.CharField(max_length=50, verbose_name='Пароль')
    role = models.CharField(max_length=9, choices=ROLES, default="member", verbose_name='Роль')
    age = models.SmallIntegerField(verbose_name='Возраст')
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Местоположение', related_name='location')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class UserSerializer(serializers.ModelSerializer):
    location_id = LocationSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'


