"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from multiprocessing.spawn import import_main_path
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('navigation', navigation ,name="navigation"),
    path('checkout', checkout ,name="checkout"),
    path('itinerary', itinerary ,name="itinerary"),
    path('login', login ,name="login"),
    path('destination', destination ,name="destination"),
    path('search', search ,name="search"),
    path('manali', manali ,name="manali"),
    path('blog', blog ,name="blog"),
     path('openblog', openblog ,name="openblog"),
    path('contactus', contactus ,name="contactus"),
    path('roadtrips', roadtrips ,name="roadtrips"),
    path('treks', treks ,name="treks"),
    path('bikingtrips', bikingtrips ,name="bikingtrips"),
    path('navigation', navigation ,name="navigation"),
    path('spititours', spititours ,name="spititours"),
    path('lehtours', lehtours ,name="lehtours"),
    path('weekendtrip', weekendtrip ,name="weekendtrip"),
    path('travelmodes', travelmodes ,name="travelmodes"),
    
    path('backpacktours', backpacktours ,name="backpacktours"),
    

    path('destination/<int:id>', destinationit ,name="destinationit"),
    
    path('aboutus', aboutus ,name="aboutus"),
    path('roadtrips/<int:id>', roaditinerary ,name="roaditinerary"),
    path('bikingtrips/<int:id>', biking ,name="biking"),
    path('treks/<int:id>', treksitinerary ,name="treksitinerary"),
    path('spititours/<int:id>', spitiitinerary ,name="spitiitinerary"),
    path('lehtours/<int:id>', lehitinerary ,name="lehitinerary"),
    path('backpacktours/<int:id>', backpackitinerary ,name="backpackitinerary"),
    path('weekendtrip/<int:id>', weekendit ,name="weekendit"),
    path('index/<int:id>', recentit ,name="recentit"),
    
    


   
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
