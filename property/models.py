from django.db import models
from broker.models import Broker
from feature.models import Feature
from neighbourhood.models import Neighbourhood
from django.core.validators import MaxValueValidator, MinValueValidator

from myhome.validators import ImageSizeValidator, ImageTypeValidator


class Property(models.Model):
    class PropertyType(models.TextChoices):
        HOUSE = "HOUSE", "House"
        APARTMENT = "APARTMENT", "Apartment"
        OFFICE = "OFFICE", "Office"
        STUDIO = "STUDIO", "Studio"
        COMMERCIAL = "COMMERCIAL", "Commercial Property"
        GARAGE = "GARAGE", "Garage"
        PLOT = "PLOT", "Plot"

    class OfferType(models.TextChoices):
        FOR_SALE = "FOR_SALE", "For Sale"
        FOR_RENT = "FOR_RENT", "For Rent"

    offer_type = models.CharField(
        max_length=20,
        choices=OfferType,
        default=OfferType.FOR_SALE,
        verbose_name="Offer Type"
    )

    property_type = models.CharField(
        max_length=20,
        choices=PropertyType,
        default=PropertyType.APARTMENT,
        verbose_name="Property Type"
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Area",
        validators=[MaxValueValidator(10000), MinValueValidator(10)],
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Price",
        validators=[MaxValueValidator(10000000), MinValueValidator(10)],
    )

    neighborhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, verbose_name="Neighbourhood")
    address = models.CharField(max_length=200, verbose_name="Address")

    bedrooms = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Bedrooms",
        validators=[
            MinValueValidator(0),
        ],
    )

    bathrooms = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Bathrooms",
        validators=[
            MinValueValidator(0),
        ],
    )

    description = models.TextField(verbose_name="Description")

    main_image = models.ImageField(
        upload_to='properties/',
        verbose_name="Picture",
        null=True,
        blank=True,
        validators=[
            ImageSizeValidator("! The image size must be less than 1 MB."),
            ImageTypeValidator("! The image format must be JPG, JPEG, or PNG.")
        ]
    )

    broker = models.ForeignKey(
        Broker,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="properties",
        verbose_name="Broker",
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    active = models.BooleanField(default=True, verbose_name="Active Listing")

    features = models.ManyToManyField(Feature, blank=True, related_name="properties", verbose_name="Features")

    def __str__(self):
        return f'{self.get_property_type_display()} {self.neighborhood} {self.price}'
