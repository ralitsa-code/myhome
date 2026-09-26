from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ["offer_type",
                  "property_type",
                  "area",
                  "price",
                  "neighborhood",
                  "address",
                  "bedrooms",
                  "bathrooms",
                  "description",
                  "broker",
                  "features",
                  "main_image",
                  ]