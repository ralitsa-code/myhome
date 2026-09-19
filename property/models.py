from django.db import models
from broker.models import Broker
from feature.models import Feature
from neighbourhood.models import Neighbourhood


class Property(models.Model):
    class PropertyType(models.TextChoices):
        HOUSE = "HOUSE", "Къща"
        APARTMENT = "APARTMENT", "Апартамент"
        OFFICE = "OFFICE", "Офис"
        STUDIO = "STUDIO", "Студио"
        COMMERCIAL = "COMMERCIAL", "Търговски обект"
        GARAGE = "GARAGE", "Гараж"
        PLOT = "PLOT", "Парцел"

    class OfferType(models.TextChoices):
        FOR_SALE = "FOR_SALE", "За продажба"
        FOR_RENT = "FOR_RENT", "Под наем"

    offer_type = models.CharField(
        max_length=20,
        choices=OfferType,
        default=OfferType.FOR_SALE,
    )

    property_type = models.CharField(
        max_length=20,
        choices=PropertyType,
        default=PropertyType.APARTMENT
    )

    area = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    neighborhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    description = models.TextField()

    broker = models.ForeignKey(
        Broker,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="properties",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    features = models.ManyToManyField(Feature, blank=True, related_name="properties")

    def __str__(self):
        return f'{self.property_type} {self.neighborhood} {self.price}'
