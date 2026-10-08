from django import forms

from myhome.mixins import DisabledFormMixin
from .models import City

class CityBaseForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["name"]


class CityCreateForm(CityBaseForm):
    ...

class CityUpdateForm(CityBaseForm):
    ...

class CityDeleteForm(DisabledFormMixin, CityBaseForm):
    ...

