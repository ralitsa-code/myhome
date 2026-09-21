from django.db import models

# Create your models here.
class Broker(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Име")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Имейл")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон")
    picture = models.ImageField(
        blank=True,
        null=True,
        verbose_name="Снимка",
        upload_to="brokers/",
    )
    description = models.TextField(verbose_name="Биография")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
