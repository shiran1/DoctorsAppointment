from datetime import date, timedelta

from django.db.models import Sum, Min
from django.shortcuts import render
from patients.models import Patient, Consultation, Billing


# Create your views here.
def index(request):
    total_patients = Patient.objects.all().count()
    total_consultations = Consultation.objects.all().count()
    total_profit = Billing.objects.all().aggregate(Sum('amount'))['amount__sum']

    give_range_profit = None
    # get yesterday's date
    yesterday = date.today() - timedelta(days=1)
    # start date
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date and end_date:
        give_range_profit = Billing.objects.filter(status__iexact="P").aggregate(Sum('amount'))['amount__sum']

    context = {
        'yersterday': yesterday,
        'start_date': start_date,
        'total_patients': total_patients,
        'total_consultations': total_consultations,
        'total_profit': total_profit,
        'range_profit' : give_range_profit,

    }
    return render(request, 'reports/index.html', context)

