from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from django import forms

from .models import Patient, Consultation, Billing


class PatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Add'))

    class Meta:
        model = Patient
        fields = ['name', 'birthday', 'contact_no', 'photo', 'nic', 'notes']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }


class ConsultationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Add'))

    class Meta:
        model = Consultation
        fields = ['diagnosis', 'treatment', 'prescription']
        widgets = {
            'diagnosis': forms.Textarea(attrs={'rows': '2'}),
            'treatment': forms.Textarea(attrs={'rows': '4'}),
            'prescription': forms.Textarea(attrs={'rows': '4'}),

        }


class BillingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Add'))

    class Meta:
        model = Billing
        fields = ['amount', 'status']
