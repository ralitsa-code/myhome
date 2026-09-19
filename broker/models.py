from django.db import models

# Create your models here.
class Broker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    picture = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
