from django.db import models
from trenirovka.models import Trenirovka
from django.contrib.auth.models import User

class Desired(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", related_name="desired", on_delete=models.CASCADE)
    name = models.ForeignKey(Trenirovka, verbose_name="Фильм", related_name="desired", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Желаемое"
        verbose_name_plural = "Желаемые"

