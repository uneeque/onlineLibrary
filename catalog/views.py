from django.shortcuts import render
from django.http import *
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.count()
    num_authors = Author.objects.count()

    return render(request, 'index.html',
                  context={
                      'num_books': num_books,
                      'num_instances': num_instances,
                      'num_instances_available': num_instances_available,
                      'num_authors': num_authors,
#                      'num_visits': num_visits
                  })


class BookListView(generic.ListView):
    model = Book

