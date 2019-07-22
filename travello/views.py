from django.shortcuts import render
from . models import Destination
# Create your views here.


def index(request):

    dest1=Destination()
    dest2=Destination()
    dest3=Destination()
    dest4=Destination()

    dest1.name = "Mumbai"
    dest2.name = "Banglore"
    dest3.name="Goa"
    dest1.img='destination_1.jpg'
    dest2.img='destination_2.jpg'
    dest3.img='destination_3.jpg'
    dests=[dest1,dest2,dest3]


    return render(request,'index.html',{'dests':dests})

