# Generated by Django 4.0.5 on 2022-06-03 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_consultation_date_consultation_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='date',
        ),
    ]
