from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from django import forms

from .models import Patient


class PatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'create'))

    class Meta:
        model = Patient
        fields = ['name', 'birthday', 'contact_no', 'photo', 'nic', 'notes']
