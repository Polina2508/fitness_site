# Generated by Django 3.1.3 on 2020-12-20 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trenirovka', '0002_auto_20201220_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='trenirovka',
            name='descriptionYoga',
            field=models.TextField(default='', verbose_name='Описание1'),
        ),
        migrations.AddField(
            model_name='trenirovka',
            name='yoga',
            field=models.CharField(default='', max_length=100, verbose_name='Название1'),
        ),
    ]
