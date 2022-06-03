from datetime import date

from django.db.models import Sum
from django.shortcuts import render
from patients.models import Patient, Consultation


# Create your views here.
def index(request):
    total_patients = Patient.objects.all().count()
    total_consultations = Consultation.objects.all().count()
    total_profit = Consultation.objects.all().aggregate(Sum('fee'))['fee__sum']
    give_range_profit = None
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date and end_date:
        give_range_profit = \
            Consultation.objects.filter(created_at__range=[start_date, end_date]).aggregate(
                Sum('fee'))['fee__sum']

    if give_range_profit:
        give_range_profit = give_range_profit
    else:
        give_range_profit = 0
    context = {

        'total_patients': total_patients,
        'total_consultations': total_consultations,
        'total_profit': total_profit,

             'last_30_days_profit': give_range_profit,
    }
    return render(request, 'reports/index.html', context)

