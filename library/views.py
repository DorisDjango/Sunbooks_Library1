from django.shortcuts import render
from .models import Author, BookInstance, Book, Language, Genre

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
        'num_of_authors': num_of_authors
    }
    
    return render(request, 'home.html', context=context)
