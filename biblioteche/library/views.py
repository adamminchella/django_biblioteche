from django.shortcuts import render, get_object_or_404
from .models import Book, Author
# Create your views here.


def home(request):
    data = {'books': Book.objects.all()}
    return render(request, "home.html", data)


def show(request, id):
    book = get_object_or_404(Book, pk=id)
    data = {"book": book}
    return render(request, 'show.html', data)


def authors(request):
    books = {'books'}


def not_found_404(request, exception):
    return render(request, "404.html")
