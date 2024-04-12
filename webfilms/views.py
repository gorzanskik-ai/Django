from django.shortcuts import render
from django.http import HttpResponse
from .models import Film

# Create your views here.

def all_films(request):
    #return HttpResponse('first test')
    all_films = Film.objects.all()
    return render(request, 'films.html', {'films': all_films}) #templates
