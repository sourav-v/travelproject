from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import teams

# Create your views here.

def demo(request):
    obj=place.objects.all()
    ob=teams.objects.all()
    return render(request, "index.html", {'result':obj,'team':ob})


