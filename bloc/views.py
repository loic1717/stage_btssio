from django.shortcuts import render
from django.http import HttpResponse
  
# Create your views here.
#URL et Request 
def home(request,*args, **kwargs):
    return render(request,'index.html')
def contact(request):
    return HttpResponse('contact me')
def blog(request):
    return HttpResponse('mon blog')