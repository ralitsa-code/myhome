from django.forms import FileInput

from django import forms

from myhome.mixins import DisabledFormMixin
from .models import Broker

class BrokerForm(forms.ModelForm):
    class Meta:
        model = Broker
        fields = ["first_name", "last_name", "email", "phone_number", "description", "picture"]

        widgets = {
            "picture": FileInput(),
            "description": forms.Textarea()
        }
        help_texts = {
            'phone_number': "Enter a phone number without spaces."
        }


class DeleteBrokerForm(DisabledFormMixin, BrokerForm):
    ...