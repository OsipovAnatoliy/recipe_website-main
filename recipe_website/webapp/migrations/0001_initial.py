# Generated by Django 4.2.7 on 2023-11-25 20:06

from django.conf import settings
from django.db import migrations, models
import webapp.models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок рецепта')),
                ('description', models.TextField(verbose_name='Описание рецепта')),
                ('ingredients', models.TextField(verbose_name='Ингредиенты')),
                ('cooking_steps', models.TextField(verbose_name='Шаги приготовления')),
                ('cooking_time', models.TimeField(verbose_name='Время приготовления')),
                ('image', models.ImageField(upload_to=webapp.models.user_directory_path, verbose_name='Изображения')),
                ('active', models.BooleanField(default=True, verbose_name='Статус активности')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.category', verbose_name='Категория')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
