
from django import forms
from django.forms import FileInput

from feature.models import Feature
from myhome.mixins import DisabledFormMixin
from .models import Property

class PropertyForm(forms.ModelForm):
    features = forms.ModelMultipleChoiceField(
        queryset=Feature.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Features",

    )
    bedrooms = forms.IntegerField(
        min_value=0,
        required=False,
        error_messages={"min_value":"! The number of bedrooms must be at least 0."}
    )

    bathrooms = forms.IntegerField(
        min_value=0,
        required=False,
        error_messages={"min_value":"! The number of bathrooms must be at least 0."}
    )

    def clean(self):
        PRICE_PER_SQUARE = 100
        cleaned_data = super().clean()
        price = cleaned_data.get("price")
        area = cleaned_data.get("area")
        if price is not None and area is not None:
            if price < area * PRICE_PER_SQUARE:
                raise forms.ValidationError("! The price is too low for the property area.")
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

class DeletePropertyForm(DisabledFormMixin, PropertyForm):
    ...