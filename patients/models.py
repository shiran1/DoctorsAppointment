from datetime import date

from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Maintain the personal details of the patients (name, birthday, contact no, photo, nic, notes)
from django.urls import reverse


class Patient(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    contact_no = models.CharField(max_length=20, validators=[MinLengthValidator(10)])
    photo = models.ImageField(upload_to='patients/photos', blank=True, null=True)
    nic = models.CharField(max_length=20, blank=True, null=True,
                           validators=[MinLengthValidator(10), MaxLengthValidator(12)])
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('patients:detail', args=[str(self.id)])

    def age(self):
        today = date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    def get_info_url(self):
        return reverse('patients:detail', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('patients:delete', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('patients:edit', args=[str(self.id)])


class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='consultations')
    diagnosis = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    prescription = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient.name

    def get_absolute_url(self):
        return reverse('patients:consultation', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('patients:consultation_delete', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('patients:consultation_edit', args=[str(self.id)])


class Billing(models.Model):
    PAID = 'P'
    UNPAID = 'U'
    STATUS_CHOICES = (
        (PAID, 'Paid'),
        (UNPAID, 'Unpaid'),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='billings')
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='billings')
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default=UNPAID)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient.name

    def get_absolute_url(self):
        return reverse('patients:billing', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('patients:billing_delete', args=[str(self.id)])