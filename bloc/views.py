from django.shortcuts import render
from django.http import HttpResponse
  
# Create your views here.
def home(request):
    return HttpResponse('<h1> Bonjour à tous </h1>')
    ##request,*args, **kwargs