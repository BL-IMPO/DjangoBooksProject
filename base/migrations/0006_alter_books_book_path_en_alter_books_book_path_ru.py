# Generated by Django 5.1.7 on 2025-03-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_books_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_path_en',
            field=models.CharField(default='\\books\\adventures\\en', max_length=400),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_path_ru',
            field=models.CharField(default='\\books\\adventures\\ru', max_length=400),
        ),
    ]
