from django.shortcuts import render
from .models import Finance
#from django.http import HttpResponse
  
# Create your views here.
#URL et Request 
def finance_list(request,*args, **kwargs):
    finance = Finance.objects.all()
    context={
    'finances': finance
    }
    return render(request, 'finance/detail.html',context)
# def contact(request):
#     return HttpResponse('contact me')
# def blog(request):
#     return HttpResponse('mon blog')