from django.shortcuts import redirect
from django.views import View
from django.views.generic.base import TemplateView 
from .models import Finch, State
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
    
class StateList(TemplateView):
    template_name = "state_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context['states'] = State.objects.filter(name__icontains=name)
            context['header'] = f"Searching for {name}"
        else: 
            context["states"] = State.objects.all()
            context["header"] = "Trending States"
        return context

class FinchCreate(CreateView):
    model = Finch
    fields = ['name','img','bio']
    template_name = "finch_create.html"
    def get_success_url(self):
            return reverse('finch_detail', kwargs={'pk': self.object.pk})

    
class FinchDetail(DetailView):
    model = Finch
    template_name = "finch_detail.html"
    
class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'img', 'bio']
    template_name = "finch_update.html"
    
    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})
    
class FinchDelete(DeleteView):
    model = Finch
    template_name = "finch_delete_confirmation.html"
    success_url = "/finchs/"
    
    
class StateFinchAssoc(View):
    
    def get(self, request, pk, finch_pk):
        assoc = request.GET.get('assoc')
        if assoc == 'remove':
            State.objects.get(pk=pk).finchs.remove(finch_pk)
        if assoc == "add":
            State.objects.get(pk=pk).finchs.add(finch_pk)
        return redirect('home')
    
    
class StateDetail(DetailView):
    model = State
    template_name = "state_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["finchs"] = Finch.objects.all()
        return context
