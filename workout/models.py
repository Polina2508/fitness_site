from django.db import models
from django.utils.safestring import mark_safe


class Trenirovka(models.Model):

    def load_video(self, filename):
        file_type = filename.split(".")[-1]
        file_name = ".".join(["{}/{}_{}_{}_{}", file_type])
        return file_name.format(
            self.name,
        )

   

    name = models.CharField(max_length=20, verbose_name="Название тренировки.")

    desc = models.TextField(verbose_name="Описание тренировки.")
   
    video = models.ImageField(upload_to=load_video, verbose_name="Тренировка.")

    class Meta:
        db_table = "trenirovka"
        verbose_name = "Тренировка"
        verbose_name_plural = "Тренировки"
