# Generated by Django 4.0.5 on 2022-06-03 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_alter_patient_birthday_alter_patient_contact_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultations', to='patients.patient'),
        ),
    ]
