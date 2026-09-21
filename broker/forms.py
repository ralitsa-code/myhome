from django.forms import FileInput

from django import forms
from .models import Broker

class BrokerForm(forms.ModelForm):
    class Meta:
        model = Broker
        fields = ["first_name", "last_name", "email", "phone_number", "description", "picture"]

        widgets = {
            "picture": FileInput(),
        }