from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Name', error_messages={"unique":"! This city has already been added."})

    def __str__(self):
        return self.name
