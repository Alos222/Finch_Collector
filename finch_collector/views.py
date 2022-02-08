from django.shortcuts import render
from django.views import View # view class to handle requests
from django.views.generic.base import TemplateView # View class to handle requests
from django.http import HttpResponse # a class to handle sending a type of response

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"