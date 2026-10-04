from django import forms
from .models import Neighbourhood

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = '__all__'





class CreateNeighbourhoodForm(forms.Form):
    name = forms.CharField(
        max_length=100,
    )
    city = forms.CharField()