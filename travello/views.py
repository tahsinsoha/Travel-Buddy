from .models import Destination
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # dest1 = Destination()
    # dest1.name='Mumbai'
    # dest1.desc='The city that never sleeps'
    # dest1.img='destination_1.jpg'
    # dest1.price=700
    # dest1.offer=False 

    # dest2 = Destination()
    # dest2.name='Bali'
    # dest2.desc='Oceans and skies'
    # dest2.img='destination_2.jpg'
    # dest2.price=1000
    # dest2.offer=False 

    # dest3 = Destination()
    # dest3.name='Norway'
    # dest3.desc='Wanna see northern lights?'
    # dest3.img='destination_3.jpg'
    # dest3.price=368
    # dest3.offer=True

    # dests = [dest1,dest2,dest3]
    dests = Destination.objects.all()
    return render(request,"index.html",{'dests': dests })

    # return render(request,"index.html",{'dest1': dest1 , 'dest2': dest2, 'dest3': dest3 })

