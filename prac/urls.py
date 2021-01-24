from django.urls import path
from prac.views import (HomeTemplateView, 
                        IndividualView, 
                        CarCreateView, 
                        CarUpdateView, 
                        CarDetailView,
                        CarDeleteView)

app_name = 'prac'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('individual/', IndividualView.as_view(), name='individual'),
    path('create/', CarCreateView.as_view(), name='create'),
    path('<int:pk>/detail/', CarDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', CarUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='delete'),
    
]



