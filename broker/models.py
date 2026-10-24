from django.db import models
from django.core.validators import RegexValidator

from myhome.validators import ImageSizeValidator, ImageTypeValidator


# Create your models here.
class Broker(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First name")
    last_name = models.CharField(max_length=100, verbose_name="Last name")
    email = models.EmailField(verbose_name="Email")
    phone_number = models.CharField(
        max_length=10,
        verbose_name="Phone number",
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="! The phone number must contain 10 digits without spaces.",
            )
        ]
    )
    picture = models.ImageField(
        blank=True,
        null=True,
        verbose_name="Picture",
        upload_to="brokers/",
        validators=[
            ImageSizeValidator("! The image size must be less than 1 MB."),
            ImageTypeValidator("! The image format must be JPG, JPEG, or PNG.")
        ]
    )
    description = models.TextField(verbose_name="Biography")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
