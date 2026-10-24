from django.db import models

from city.models import City


class Neighbourhood(models.Model):
    name = models.CharField(max_length=100, verbose_name="Neighbourhood")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='neighbourhoods', verbose_name="City")


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['city', 'name'],
                name='unique_neighbourhood_per_city',
                violation_error_message= '! This neighbourhood has already been added.',
            )
        ]

    def __str__(self):
        return f"{self.name} - {self.city}"
