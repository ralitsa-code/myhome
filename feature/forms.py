from django import forms

from myhome.mixins import DisabledFormMixin
from .models import Feature

class FeatureBaseForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ["name"]

class CreateFeatureForm(FeatureBaseForm):
    ...

class UpdateFeatureForm(FeatureBaseForm):
    ...

class DeleteFeatureForm(DisabledFormMixin, FeatureBaseForm):
    ...