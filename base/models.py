from django.db import models

# Create your models here.


class Authors(models.Model):
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.author


class Genres(models.Model):
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.genre


class Books(models.Model):
    book_title = models.TextField(null=False)
    book_author = models.ForeignKey(Authors, on_delete=models.SET_NULL, null=True)
    book_genre = models.ForeignKey(Genres, on_delete=models.SET_NULL, null=True)
    book_description = models.TextField(null=True, default="Not found!")
    book_path_ru = models.CharField(max_length=400, null=False, default="\\books\\adventures\\ru")
    book_path_en = models.CharField(max_length=400, null=False, default="\\books\\adventures\\en")
    book_cover = models.ImageField(default='books_cover.jpg', blank=True)

    def __str__(self):
        return self.book_title

