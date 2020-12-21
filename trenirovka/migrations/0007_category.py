# Generated by Django 3.1.3 on 2020-12-21 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trenirovka', '0006_auto_20201221_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
