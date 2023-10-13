from django.shortcuts import render
from .models import destination
# Create your views here.


def home(request):
    data = destination.objects.all()
    return render(request,'home.html',{'dest':data})

def item(request):
    data = destination.objects.all()
    return render(request,'item.html',{'dest':data})