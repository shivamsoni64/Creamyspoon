from django.shortcuts import render, HttpResponse
from datetime import datetime
from app1.models import Contact,Pro
from django.contrib import messages
import time


def index(request):
    datas= Pro.objects.all()
    time.sleep(2)
    
    return render(request,'index.html',{'datas':datas})

def varieties(request):
    return render(request, "varieties.html")

def blogs(request):
    return render(request, "blogs.html")

def knowus(request):
    return render(request, "knowus.html")

def contactus(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact= Contact( name= name, email= email, phone= phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, "contactus.html")