from django.db.models import Sum
from django.shortcuts import render

# create class based view for create a new patient
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Patient, Consultation, Billing
from .forms import PatientForm, ConsultationForm, BillingForm
from .filters import PatientFiler


class CreatePatientView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/form.html'
    success_url = '/patients/'


class ListPatientsView(ListView):
    model = Patient
    template_name = 'patients/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PatientFiler()
        context['patients_qs'] = self.get_queryset
        return context

    def get_queryset(self):
        qs = Patient.objects.all().order_by('-updated_at')
        patient_filter = PatientFiler(self.request.GET, queryset=qs)
        return patient_filter.qs


class UpdatePatientView(UpdateView):
    model = Patient
    template_name = 'patients/form.html'
    form_class = PatientForm


class DeletePatientView(DeleteView):
    model = Patient
    template_name = 'patients/delete.html'
    success_url = '/patients/'


class DetailPatientView(DetailView):
    model = Patient
    template_name = 'patients/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs['pk'])
        context['consultations'] = context['patient'].consultations.all()
        context['due_billing'] = context['patient'].billings.filter(status='U').aggregate(Sum('amount'))['amount__sum']
        return context


class CreateConsultationView(CreateView):
    model = Consultation
    form_class = ConsultationForm
    template_name = 'diagnoses/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs['patient_pk'])
        context['consultations'] = context['patient'].consultations.all()
        return context

    def get_success_url(self):
        return '/patients/{}/'.format(self.kwargs['patient_pk'])

    def form_valid(self, form):
        form.instance.patient = Patient.objects.get(pk=self.kwargs['patient_pk'])
        return super().form_valid(form)


class DetailConsultationView(DetailView):
    model = Consultation
    template_name = 'diagnoses/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs['patient_pk'])
        context['consultation'] = context['patient'].consultations.get(pk=self.kwargs['pk'])
        return context


class ListConsultationView(ListView):
    model = Patient
    template_name = 'diagnoses/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs['patient_pk'])
        context['consultations'] = Patient.objects.get(pk=self.kwargs['patient_pk']).consultations.all()
        return context


class UpdateConsultationView(UpdateView):
    model = Consultation
    template_name = 'diagnoses/form.html'
    form_class = ConsultationForm

    def get_success_url(self):
        return '/patients/{}/'.format(self.kwargs['patient_pk'])

    def form_valid(self, form):
        form.instance.patient = Patient.objects.get(pk=self.kwargs['patient_pk'])
        return super().form_valid(form)


class DeleteConsultationView(DeleteView):
    model = Consultation
    template_name = 'diagnoses/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs['patient_pk'])
        return context

    def get_success_url(self):
        return '/patients/{}/'.format(self.kwargs['patient_pk'])


class CreateBillingView(CreateView):
    model = Billing
    form_class = BillingForm
    template_name = 'billing/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs['patient_pk'])
        context['consultations'] = context['patient'].consultations.all()
        return context

    def get_success_url(self):
        return '/patients/{}/'.format(self.kwargs['patient_pk'])

    def form_valid(self, form):
        form.instance.patient = Patient.objects.get(pk=self.kwargs['patient_pk'])
        form.instance.consultation = Consultation.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
