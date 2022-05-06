# Generated by Django 4.0.3 on 2022-05-07 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movieshorts_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieshorts',
            name='image',
            field=models.ImageField(upload_to='movie_shots/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='movieshorts',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]