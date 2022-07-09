
from django.shortcuts import render, get_object_or_404
from .models import Author, BookInstance, Book, Language, Genre
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

    
def home(request):
    num_of_books = Book.objects.all().count()
    num_of_book_instances = BookInstance.objects.all().count()
    num_of_book_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_of_authors = Author.objects.count()
    
    context = {
        'num_of_books': num_of_books,
        'num_of_book_instances': num_of_book_instances,
        'num_of_book_instances_available': num_of_book_instances_available,
        'num_of_authors': num_of_authors,
    } 
    
    
    
    return render(request, 'home.html', context=context)

    
def BookList(request):
    books = Book.objects.all()
    
    context = {
        'books': books
    }
    
    return render(request, 'books.html', context=context)


def BookDetail(request,pk=None):
    book_detail = get_object_or_404(Book, pk=pk)
    
    context = {
        'book_detail': book_detail
    }
    
    return render(request, 'book_detail.html', context=context)

def AuthorList(request):
    authors = Author.objects.all()
    
    context = {
        'authors': authors
    }
    
    return render(request, 'authors.html', context=context)
    

def AuthorDetail(request, pk=None):
    author_detail = get_object_or_404(Author, pk=pk)
    
    context = {
        'author_detail': author_detail
    }
    
    return render(request, 'author_detail.html', context=context)
