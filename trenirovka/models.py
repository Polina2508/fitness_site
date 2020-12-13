
from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User



class Trenirovka(models.Model):

    title = models.CharField(verbose_name="Название", max_length=100)
    url = models.SlugField(max_length=130, unique=True)
    description = models.TextField(verbose_name="Описание" , default="")

    def __str__(self):
        return f"{self.title} - {self.description}"

    def get_absolute_url(self):
        return reverse('add_desired', kwargs={'slug': self.url})


    class Meta:
        verbose_name = "Тренировка"
        verbose_name_plural = "Тренировки"