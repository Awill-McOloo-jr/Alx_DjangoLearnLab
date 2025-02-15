from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add search functionality for 'title' and 'author'
    search_fields = ('title', 'author')

    # Add filter options for 'publication_year'
    list_filter = ('publication_year',)


# Register your models here.

admin.site.register(Book, BookAdmin)
