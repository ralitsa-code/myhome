from django.db import models
from broker.models import Broker
from feature.models import Feature
from neighbourhood.models import Neighbourhood
from django.core.validators import MaxValueValidator, MinValueValidator


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
        verbose_name="Тип оферта"
    )

    property_type = models.CharField(
        max_length=20,
        choices=PropertyType,
        default=PropertyType.APARTMENT,
        verbose_name="Тип имот"
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Площ",
        validators=[MaxValueValidator(10000), MinValueValidator(10)],
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        validators=[MaxValueValidator(10000000), MinValueValidator(10)],
    )

    neighborhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, verbose_name="Квартал")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    bedrooms = models.IntegerField(null=True, blank=True, verbose_name="Спални")
    bathrooms = models.IntegerField(null=True, blank=True, verbose_name="Бани")
    description = models.TextField(verbose_name="Описание")

    main_image = models.ImageField(
        upload_to='properties/',
        verbose_name="Снимка",
        null=True,
        blank=True)

    broker = models.ForeignKey(
        Broker,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="properties",
        verbose_name="Брокер",
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата на създаване")
    active = models.BooleanField(default=True, verbose_name="Активна оферта")

    features = models.ManyToManyField(Feature, blank=True, related_name="properties", verbose_name="Характеристики")

    def __str__(self):
        return f'{self.get_property_type_display()} {self.neighborhood} {self.price}'
