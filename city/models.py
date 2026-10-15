from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Име', error_messages={"unique":"! Този град вече е добавен."})

    def __str__(self):
        return self.name
