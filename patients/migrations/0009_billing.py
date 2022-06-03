# Generated by Django 4.0.5 on 2022-06-03 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0008_patient_created_at_patient_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('status', models.CharField(choices=[('P', 'Paid'), ('U', 'Unpaid')], default='U', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billings', to='patients.consultation')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billings', to='patients.patient')),
            ],
        ),
    ]