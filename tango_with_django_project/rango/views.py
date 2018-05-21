from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
#request is a HttpRequest object
#each view should return a HttpResponse object
def index(request):
    return HttpResponse("Rango says hey there parterner!")
