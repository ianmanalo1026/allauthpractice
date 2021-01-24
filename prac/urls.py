from django.urls import path
from prac.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home')
]



