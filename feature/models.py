from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=20, unique=True, error_messages={'unique': '! This feature has already been added.'})

    def __str__(self):
        return self.name
