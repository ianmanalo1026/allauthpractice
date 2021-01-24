
from typing import ContextManager
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView,  DetailView
from prac.models import Car

class HomeTemplateView(TemplateView):
    
    model = Car
    template_name = 'prac/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = Car.objects.all()
        return context
    

class IndividualView(TemplateView):
    model = Car
    template_name = 'prac/individual.html'
    
    def get(self, request, *args, **kwargs):
        context = Car.objects.filter(owner=self.request.user)
        return render(request, self.template_name, {'context':context})
    
    
class CarCreateView(CreateView):
    model = Car
    template_name = 'prac/create.html'
    fields = ['name', 'brand', 'model', 'year']
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CarCreateView, self).form_valid(form)
    
class CarDetailView(DetailView):
    
class CarUpdateView(UpdateView):
    model = Car
    template_name = 'prac/update.html'
    fields = ['name', 'brand', 'model', 'year']
    success_url = '/'
    
    def get_object(self, queryset=None):
        return self.request.user
    
            
    
