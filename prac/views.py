
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from prac.models import Car

class HomeTemplateView(TemplateView):
    
    model = Car
    template_name = 'prac/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = Car.objects.all()
        return context
    
    
