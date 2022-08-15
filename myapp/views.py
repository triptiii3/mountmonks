import email
from http.client import HTTPResponse
import re
from unicodedata import name
from django.shortcuts import render, HttpResponse


from .models import saveEnquiry
from destinations.models import destinations,Manali
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import Contact, bikingtours, roadtours , trekking, spititrip, lehtrip, backpacktrip, weekendtrip

# Create your views here.

def index(request):
    return render(request, 'index.html')
def navigation(request):
    return render(request, 'navigation.html')
def contactus(request):
    
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(message)<4:
            messages.error(request, "Please fill the form correctly")
        else:
           contact=Contact(name=name,email=email,phone=phone,message=message)
           contact.save()
           messages.success(request,"We will reach to you shortly.")
    return render(request, 'contactus.html')
def roadtrips(request):
    roadtourData=roadtours.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            roadtourData=roadtours.objects.filter(destination_title__icontains= st)
    
    data={
        'roadtourData':roadtourData
    }
    
    return render(request, 'roadtrips.html',data)
def treks(request):
    trekkingData=trekking.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            trekkingData=trekking.objects.filter(destination_title__icontains= st)
    
    data={
        'trekkingData':trekkingData
    }
    return render(request, 'treks.html',data)
def bikingtrips(request):
    bikingtourData=bikingtours.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            bikingtourData=bikingtours.objects.filter(destination_title__icontains= st)
    
    data={
        'bikingtourData':bikingtourData
    }
    return render(request, 'bikingtrips.html',data)
def destination(request):
    destinationData=destinations.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            destinationData=destinations.objects.filter(destination_title__icontains= st)
    
    data={
        'destinationData':destinationData
    }
    

    return render(request, 'destination.html',data)
def openblog(request):
    
    return render(request, 'openblog.html')
def login(request):
    
    return render(request, 'login.html')

def blog(request):
    
    return render(request, 'blog.html')

def search(request):
   
    return render(request,'search.html')

def manali(request):
   
    return render(request,'manali.html')
def navigation(request):
   
    return render(request,'navigation.html')
def aboutus(request):
   
    return render(request,'aboutus.html')
def leh(request):
    manalidata=Manali.objects.all()
    data={
        'manalidata': manalidata
    }
    return render(request,'leh.html',data)
def spititours(request):
    spititripData=spititrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            spititripData=spititrip.objects.filter(destination_title__icontains= st)
    
    data={
        spititripData:'spititripData'
    }
   
    return render(request,'spititours.html',data)
def lehtours(request):
    lehtripData=lehtrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            lehtripData=lehtrip.objects.filter(destination_title__icontains= st)
    
    data={
        lehtripData:'lehtripData'
    }
   
    return render(request,'lehtours.html',data)
def backpacktours(request):
    lehtripData=lehtrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            lehtripData=lehtrip.objects.filter(destination_title__icontains= st)
    
    data={
        lehtripData:'lehtripData'
    }
   
    return render(request,'backpacktours.html',data)
def weekendtours(request):
    weekendtripData=weekendtrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            weekendtripData=weekendtrip.objects.filter(destination_title__icontains= st)
    
    data={
        weekendtripData:'weekendtripData'
    }
    return render(request,'weekendtours.html',data)
    
def itinerary(request):
    

    if request.method=="POST":
        
        name = request.POST['name']
        email=request.POST['email']
        dates=request.POST['dates']
        number=request.POST.get('number')
        ins=saveEnquiry(name=name, email=email,dates=dates, number=number)
        ins.save()
        
        messages.success(request,"We will reach to you shortly")
        print("the data has been saved to db")
    return render(request, 'itinerary.html')


