from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
"""
# -*- coding: utf-8 -*-
# Create your models here.
class Languages(models.Model):
    Model representing a language.
    lang = models.CharField(max_length=20, help_text='Enter language (e.g. USA)')
    
    def __str__(self):
        String for representing the Model object.
        return self.lang
"""
class Navibar(models.Model):
    """Model representing a menu genre."""
    name = models.CharField(max_length=50, help_text='Enter a menu genre (e.g. Home, About Us)')
    sort = models.IntegerField()
    languages = (
        (0, 'VN'),
        (1, 'USA'),        
    )

    lang = models.BooleanField(        
        choices=languages,
        #blank=True,
        default='0',
        help_text='Language availability',
    )

    def clean(self):
        """
        Custom validation (read docs)
        PS: why do you have null=True on charfield? 
        we could avoid the check for name
        """
        if self.name: 
            self.name = self.name.strip()
            #print(len(self.name))

    class Meta:
        ordering = ['sort']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

#from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Post(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    navibar = models.ForeignKey('Navibar', on_delete=models.SET_NULL, null=True)
    #description = models.TextField(help_text='Enter a description of the major', null=True, blank = True)
    #description = RichTextField(null=True, blank = True)
    description = RichTextUploadingField(null=True, blank = True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book', null=True, blank = True)        
    slug = models.SlugField(null=True, blank = True, allow_unicode = True)    
    created = models.DateField(auto_now_add=True)

    option = (
        (0, 'Hide'),
        (1, 'Visible'),        
    )

    visibility = models.BooleanField(        
        choices=option,
        #blank=True,
        default='1',
        help_text='Post availability',
    )

    class Meta:
        ordering = ['created']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.title})'

class Course(models.Model):  
    coursename = models.CharField(max_length=50, help_text='Enter a name')
    code = models.CharField(max_length=50, help_text='Enter a code')
    discription = models.TextField(max_length=1000, help_text='Enter a brief description of the course', null=True, blank = True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['coursename']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.coursename}'


