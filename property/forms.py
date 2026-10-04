from django import forms
from django.forms import FileInput

from feature.models import Feature
from .models import Property

class PropertyForm(forms.ModelForm):
    features = forms.ModelMultipleChoiceField(
        queryset=Feature.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
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

        }

