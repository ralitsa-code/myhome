from django.db import models

from city.models import City


class Neighbourhood(models.Model):
    name = models.CharField(max_length=100, verbose_name="Квартал")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='neighbourhoods', verbose_name="Град")


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['city', 'name'],
                name='unique_neighbourhood_per_city',
            )
        ]

    def __str__(self):
        return f"{self.name} - {self.city}"
