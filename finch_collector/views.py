from django.shortcuts import redirect
from django.views import View # view class to handle requests
from django.views.generic.base import TemplateView # View class to handle requests
from django.http import HttpResponse # a class to handle sending a type of response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse




# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class FinchList(TemplateView):
    template_name = "finch_list.html"

    def get_context_date(self, **kwargs):
        context = super().get.context_date(**kwargs)
        context["finchs"] = finchs

        return context

class Finch:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio


finchs = [
  Finch("Gorillaz", "https://i.scdn.co/image/ab67616d00001e0295cf976d9ab7320469a00a29",
          "Gorillaz are once again disrupting the paradigm and breaking convention in their round the back door fashion with Song Machine, the newest concept from one of the most inventive bands around.")
]