import django_filters
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Patient


class PatientFiler(django_filters.FilterSet):
    class Meta:
        model = Patient
        fields = {
            'name': ['icontains'],
            'nic': ['icontains'],
            'contact_no': ['icontains'],
        }


