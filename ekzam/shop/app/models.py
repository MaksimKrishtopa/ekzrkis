from django.contrib.auth.models import AbstractUser
from django.db import models


class AdvUser(AbstractUser):
    photo = models.ImageField(verbose_name="Фото", blank=False, upload_to='user/')


class Product(models.Model):
    name = models.CharField(verbose_name="Название товара", max_length=50)
    desc = models.CharField(verbose_name="Описание товара", max_length=200)
    photo = models.ImageField(verbose_name="Фото", blank=False, upload_to='product/')
    date_creation = models.DateTimeField(verbose_name="Дата создания товара", auto_now_add=True)


class Order(models.Model):
    user = models.ForeignKey(AdvUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
