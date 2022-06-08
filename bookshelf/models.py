from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, help_text="Title of the book")
    authors = models.CharField(max_length=200, help_text="Authors of the book")
    acquired = models.BooleanField(default=False, verbose_name="Status of the book: acquired?")
    publication_date = models.DateField(verbose_name="Publication date of the book.", null=True, blank=True)
    thumbnail = models.URLField(blank=True, verbose_name="URL to thumbnail of the book")
