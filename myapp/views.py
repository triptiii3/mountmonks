import email
from http.client import HTTPResponse
import re
from unicodedata import name
from django.shortcuts import render, HttpResponse


from .models import saveEnquiry
from destinations.models import destinations
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import Contact, bikingtours, roadtours , trekking, spiti, lehtrip, backpack, weekend, populartours , recenttours

# Create your views here.

def index(request):
    
        
        
    populartoursData=populartours.objects.all()
    recenttoursData=recenttours.objects.all()
   
    
    data={
        'recenttoursData':recenttoursData, 'populartoursData':populartoursData
    }
    return render(request, 'index.html',data)
def recentit(request,id):
    
    recenttoursData=recenttours.objects.filter(id=id)
    data={
        'recenttoursData':recenttoursData
    }
    return render(request,'recentit.html',data)
def navigation(request):
    return render(request, 'navigation.html')
def travelmodes(request):
    name=request.GET.get('name')
    email=request.GET.get('email')
    people=request.GET.get('people')
    mode=request.GET.get('mode')
    batch=request.GET.get('batch')
   
    
                
    
    return render(request, 'travelmodes.html',{'name':name,'email':email,'people':people,'mode':mode,'batch':batch})
def checkout(request):
    roadtourData=roadtours.objects.all()
    name=request.GET.get('name')
    email=request.GET.get('email')
    people=request.GET.get('people')
    mode=request.GET.get('mode')
    batch=request.GET.get('batch')
    destination=request.GET.get('destination')
    
    data={
        'roadtourData':roadtourData,'name':name,'email':email,'people':people,'mode':mode,'batch':batch,'destination':destination
    }
   
    
    return render(request, 'checkout.html',data)
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
            roadtourData=roadtours.objects.filter(destination__icontains= st)
    
    data={
        'roadtourData':roadtourData
    }
    
    return render(request, 'roadtrips.html',data)
def treks(request):
    trekkingData=trekking.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            trekkingData=trekking.objects.filter(destination__icontains= st)
    
    data={
        'trekkingData':trekkingData
    }
    return render(request, 'treks.html',data)
def bikingtrips(request):
    bikingtourData=bikingtours.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            bikingtourData=bikingtours.objects.filter(destination__icontains= st)
    
    data={
        'bikingtourData':bikingtourData
    }
    return render(request, 'bikingtrips.html',data)
def destination(request):
    destinationData=destinations.objects.all()
    
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            destinationData=destinations.objects.filter(destination__icontains= st)
    
    data={
        'destinationData':destinationData
    }
    

    return render(request, 'destination.html',data)
def spititours(request):
    spitiData=spiti.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            spitiData=spiti.objects.filter(destination__icontains= st)
    
    data={
        'spitiData':spitiData
    }
    return render(request, 'spititours.html',data)
def spitiitinerary(request,id):
    
    spitiData=spiti.objects.filter(id=id)
    data={
        'spitiData': spitiData
    }
    return render(request,'spitiitinerary.html',data)
def lehtours(request):
    lehtripData=lehtrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            lehtripData=lehtrip.objects.filter(destination__icontains= st)
    
    data={
        'lehtripData':lehtripData
    }
    return render(request, 'lehtours.html',data)
def lehitinerary(request,id):
    
    lehtripData=lehtrip.objects.filter(id=id)
    data={
        'lehtripData': lehtripData
    }
    return render(request,'lehitinerary.html',data)
def backpacktours(request):
    backpackData=backpack.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            backpackData=backpack.objects.filter(destination__icontains= st)
    
    data={
        'backpackData':backpackData
    }
    return render(request, 'backpacktours.html',data)
def backpackitinerary(request,id):
    
    backpackData=backpack.objects.filter(id=id)
    data={
        'backpackData': backpackData
    }
    return render(request,'backpackitinerary.html',data)

def weekendtrip(request):
    weekendData=weekend.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            weekendData=weekend.objects.filter(destination__icontains= st)
    
    data={
        'weekendData':weekendData
    }
    return render(request, 'weekendtrip.html',data)
def weekendit(request,id):
    
    weekendData=weekend.objects.filter(id=id)
    data={
        'weekendData': weekendData
    }
    return render(request,'weekendit.html',data)

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
def destinationit(request,id):
    
    destinationData=destinations.objects.filter(id=id)
    data={
        'destinationData': destinationData
    }
    return render(request,'destinationit.html',data)


def roaditinerary(request,id):
    
    roadtourData=roadtours.objects.filter(id=id)
    data={
        'roadtourData': roadtourData
    }
    return render(request,'roaditinerary.html',data)

def treksitinerary(request,id):
    
    trekkingData=trekking.objects.filter(id=id)
    data={
        'trekkingData': trekkingData
    }
    return render(request,'treksitinerary.html',data)


   
def biking(request,id):
    
    bikingtourData=bikingtours.objects.filter(id=id)
    data={
        'bikingtourData': bikingtourData
    }
    return render(request,'biking.html',data)

    
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


