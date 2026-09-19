from django.db import models

from city.models import City


class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='neighbourhoods')


    def __str__(self):
        return self.name
