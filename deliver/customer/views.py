from django.shortcuts import render
from django.views import view

class Index(view):
    def get (self, request , *args, **kwargs):
        return render (request, 'customer/index.html')
    
class About(view):
    def get (self, request , *args, **kwargs):
         return render (request, 'customer/about.html')
      
