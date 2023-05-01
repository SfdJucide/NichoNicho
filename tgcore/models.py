from django.db import models
from datetime import datetime


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    short_description = models.TextField(blank=True, verbose_name="Описание")
    long_description = models.TextField(blank=True)
    available = models.BooleanField(default=True, verbose_name="Активный")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Последнее обновление")

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return f'{self.name}'


class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products', blank=True, verbose_name='Картинка')


class TgUser(models.Model):
    user_id = models.BigIntegerField()
    username = models.CharField(max_length=100, null=True, verbose_name="Пользователь")
    register_date = models.DateTimeField(auto_now=True, verbose_name="Дата регистрации")

    class Meta:
        verbose_name = 'TG Пользователь'
        verbose_name_plural = 'TG Пользователи'

    def __str__(self) -> str:
        return f'{self.username}'
    

class CustomerMessage(models.Model):
    user = models.ForeignKey(TgUser, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField(verbose_name='Сообщение')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

