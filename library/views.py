
from django.shortcuts import render, get_object_or_404
from .models import Author, BookInstance, Book, Language, Genre
from django.views import generic

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
    } #its closed surely
    
    
    
    return render(request, 'home.html', context=context)

    

def BookList(request):
    book_list = Book.objects.all()
    
    context = {
        'book_list': book_list
    }
    return render(request, 'books.html', context=context)

def BookDetail(request,pk=None):
    book_detail = get_object_or_404(Book, pk=pk)
    
    context = {
        'book_detail': book_detail
    }
    
    return render(request, 'book_detail.html', context=context)
    


