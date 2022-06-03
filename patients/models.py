from django.db import models


# Maintain the personal details of the patients (name, birthday, contact no, photo, nic, notes)
class Patient(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    contact_no = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='patients/photos')
    nic = models.CharField(max_length=20)
    notes = models.TextField()

    def __str__(self):
        return self.name