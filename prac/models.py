from django.db import models
from django.conf import settings


class Car(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.DateField()
    
    
    def __str__(self):
        return self.owner.first_name