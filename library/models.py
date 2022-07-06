from tracemalloc import get_traced_memory
from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the a genre eg 'Science', 'Fiction'")
    
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100, help_text="Write the language eg English, French, Kiswahili")
    
    def __str__(self):
        return self.name    

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book", blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    
    GRADE_LEVEL = (
        ('1', 'Grade 1'),
        ('2', 'Grade 2'),
        ('3', 'Grade 3'),
        ('4', 'Grade 4'),
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
        
    )
    
    grade = models.CharField(max_length=1, choices=GRADE_LEVEL, blank=True, default='2', help_text="Grade Level")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])
    
class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for book across the library")
    due_back = models.DateField(null=True, blank=True)
    
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('b' , 'Borrowed'),
        ('a' , 'Available'),
        ('r' , 'Reserved')
    )
    
    status = models.CharField(max_length=1,
                              choices=LOAN_STATUS,
                              blank=True,
                              default='m',
                              help_text='Book Availability',
                              )
    
    class Meta:
        ordering = ['due_back']
        
    def __str__(self):
        return f'{self.book.title}, [{self.id}]'
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000, null=True)
    
    class Meta:
        ordering = ['first_name', 'last_name']
    
    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
    
