from django.contrib import admin

from .models import Film

# Register your models here.

#admin.site.register(Film)
@admin.register(Film)

class FilmAdmin(admin.ModelAdmin):
    #fields = ['title', 'year']
    #exclude = ['description']
    #list_display = ['title', 'year', 'imdb_rating']
    #list_filter = ['imdb_rating', 'year']
    search_fields = ['title']