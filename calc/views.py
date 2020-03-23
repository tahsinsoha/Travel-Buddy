from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Navin'})

def add(request):
        val1 =int( request.POST["num1"] )# here use the get method of dictionary see in python docs
        val2 = int(request.POST["num2"]) # also same change use get method num2 is key and 1 is default value 
        res = val1 + val2
        return render(request,"result.html",{"result": res})