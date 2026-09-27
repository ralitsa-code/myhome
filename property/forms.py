from django import forms
from django.forms import FileInput

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
                  "active",
                  ]

        widgets = {
            "main_image": FileInput(),
            "active": forms.CheckboxInput(attrs={"disabled": True}),
        }

