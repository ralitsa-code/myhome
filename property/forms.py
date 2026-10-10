
from django import forms
from django.forms import FileInput

from feature.models import Feature
from .models import Property

class PropertyForm(forms.ModelForm):
    features = forms.ModelMultipleChoiceField(
        queryset=Feature.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Характеристики",

    )

    def clean(self):
        PRICE_PER_SQUARE = 100
        cleaned_data = super().clean()
        price = cleaned_data.get("price")
        area = cleaned_data.get("area")
        if price and area:
            if price < area * PRICE_PER_SQUARE:
                raise forms.ValidationError("Цената е прекалено ниска, спрямо площта.")
        return cleaned_data

    class Meta:
        model = Property
        fields = ["offer_type", "property_type", "area", "price", "neighborhood", "address",
                  "bedrooms", "bathrooms", "description", "broker", "features", "main_image",
                  "active",
                  ]

        widgets = {
            "main_image": FileInput(),

        }

