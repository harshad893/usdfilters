from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def usd(request):
    d={'data':'hai HOW Are YoU'}
    return render(request,'usd.html',d)

def wish(request,name):
    return HttpResponse(f'hai this is {name}')