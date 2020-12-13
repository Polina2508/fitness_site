from django.db import models
from django.contrib.auth.models import User

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    

    def __str__(self):
        return f"{self.name} - {self.text}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"