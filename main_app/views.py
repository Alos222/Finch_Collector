from django.shortcuts import redirect
from django.views import View
from django.views.generic.base import TemplateView 
from .models import Finch
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse


class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class FinchList(TemplateView):
    template_name = "finch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["finchs"] = Finch.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["finchs"] = Finch.objects.all()
            context["header"] = "Trending finchs"
        return context

class FinchCreate(CreateView):
    model = Finch
    fields = ['name','img','bio']
    template_name = "finch_create.html"
    sucess_url = "/finchs/"