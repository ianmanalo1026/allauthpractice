from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (TemplateView, 
                                  CreateView, 
                                  UpdateView, 
                                  DetailView, 
                                  DeleteView)
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
    model = Car
    template_name = 'prac/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    template_name = 'prac/update.html'
    fields = ['name', 'brand', 'model', 'year']
    success_url = '/'
    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False
    

class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    template_name = "prac/delete.html"
    
    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Car, pk=pk_)
    
    def get_success_url(self):
        return reverse("prac:home")
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        else:
            return False
            
    
