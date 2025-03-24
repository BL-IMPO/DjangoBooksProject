from django.shortcuts import render, redirect
from django.db.models import Q
from PyPDF2 import PdfReader
# local
from .models import Authors, Genres, Books
# Create your views here.


def get_book_path(book_path):
    import os
    return os.path.abspath(os.getcwd()) + book_path + '.pdf'


def get_text(ru_book_path, en_book_path, page):
    path_ru = get_book_path(ru_book_path)
    path_en = get_book_path(en_book_path)

    reader_ru = PdfReader(path_ru)
    reader_en = PdfReader(path_en)

    text_ru_raw = reader_ru.pages[page]
    text_en_raw = reader_en.pages[page]
    text_en = text_en_raw.extract_text()
    text_ru = text_ru_raw.extract_text()

    return text_ru, text_en


def get_pages(ru_book_path, en_book_path):
    path_ru = get_book_path(ru_book_path)
    path_en = get_book_path(en_book_path)

    reader_ru = PdfReader(path_ru)
    reader_en = PdfReader(path_en)

    pages = len(reader_en.pages)
    return pages


def about(request):
    return render(request, 'base/about.html')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    books = Books.objects.filter(
        Q(book_author__author__icontains=q)|
        Q(book_title__icontains=q)|
        Q(book_genre__genre__icontains=q)
    )

    context = {'books': books}
    return render(request, 'base/home.html', context)


def book(request, pk, p):
    book = Books.objects.get(id=pk)
    page = p

    try:
        page_search = int(request.GET.get('page') if request.GET.get('page') != None else '')
    except:
        page_search = p

        print("Can't convert page_search in int!")

    pages_ru = get_pages(book.book_path_ru, book.book_path_ru)
    pages_en = get_pages(book.book_path_ru, book.book_path_en)
    pages = min([pages_en, pages_ru])

    if p != page_search:
        if 0 < page_search < pages:
            page = page_search
    else:
        page = p

    text_ru, text_en = get_text(book.book_path_ru, book.book_path_en, page-1)

    context = {'book': book, 'text_ru': text_ru, 'text_en': text_en, 'pages': pages, 'page': page}
    return render(request, 'base/book.html', context)
