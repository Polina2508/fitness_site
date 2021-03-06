# Generated by Django 3.1.3 on 2020-12-13 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trenirovka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desired',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desired', to='trenirovka.trenirovka', verbose_name='Фильм')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desired', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Желаемое',
                'verbose_name_plural': 'Желаемые',
            },
        ),
    ]
