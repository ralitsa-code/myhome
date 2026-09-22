from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Broker(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Име")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Имейл")
    phone_number = models.CharField(
        max_length=10,
        verbose_name="Телефон",
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="Моля въведете 10-цифрен номер без интервали",
            )
        ]
    )
    picture = models.ImageField(
        blank=True,
        null=True,
        verbose_name="Снимка",
        upload_to="brokers/",
    )
    description = models.TextField(verbose_name="Биография")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
