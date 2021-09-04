# Generated by Django 3.0.5 on 2021-06-12 06:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid
import yamdb.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование категории')),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True, verbose_name='URL slug')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200, verbose_name='Тукст комментария')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата комментария')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='наименование жанра')),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True, verbose_name='URL slug')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='GenreTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200, verbose_name='Текст отзыва')),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Минимальное значение: 0 баллов'), django.core.validators.MaxValueValidator(10, 'Максимальное значение: 10 баллов')], verbose_name='Текст отзыва')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата отзыва')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название произведения')),
                ('year', models.SmallIntegerField(validators=[yamdb.validators.validate_year], verbose_name='Год выхода')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание произведения')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='yamdb.Category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(to='yamdb.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
            },
        ),
    ]
