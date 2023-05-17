from django.shortcuts import render
from .models import Finance
#from django.http import HttpResponse
  
# Create your views here.
#URL et Request 
def finance_list(request,*args, **kwargs):
    finance = Finance.objects.get.all()
    context={
'name':finance.name,
'price':finance.price,
'image':finance.image
    }
    return render(request, 'finance/detail.html',context)
# def contact(request):
#     return HttpResponse('contact me')
# def blog(request):
#     return HttpResponse('mon blog')