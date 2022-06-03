from django.contrib import admin

from .models import Patient, Consultation, Billing

admin.site.register(Patient)
admin.site.register(Consultation)
admin.site.register(Billing)
