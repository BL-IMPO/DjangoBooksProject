from django.contrib import admin

# Register your models here.
from .models import Authors, Books, Genres

admin.site.register(Authors)
admin.site.register(Genres)
admin.site.register(Books)