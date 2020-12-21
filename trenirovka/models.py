
from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):

    name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=160, unique=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Trenirovka(models.Model):

    title = models.CharField(verbose_name="Название", max_length=100)
    url = models.SlugField(max_length=130, unique=True)
    description = models.TextField(verbose_name="Описание",default='')
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title} {self.description}"

    def get_absolute_url(self):
        return reverse('add_desired', kwargs={'slug': self.url})


    class Meta:
        verbose_name = "Тренировка"
        verbose_name_plural = "Тренировки"


