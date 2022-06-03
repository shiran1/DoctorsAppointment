from django.urls import path

from . import views

app_name = 'patients'
urlpatterns = [
    path('', views.ListPatientsView.as_view(), name='list'),
    path('create/', views.CreatePatientView.as_view(), name='create'),
    path('<int:pk>/', views.DetailPatientView.as_view(), name='detail'),
    path('<int:pk>/update/', views.UpdatePatientView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.DeletePatientView.as_view(), name='delete'),

    path('<int:patient_pk>/diagnose/create/', views.CreateConsultationView.as_view(), name='diagnose_create'),
    path('<int:patient_pk>/diagnose/', views.ListConsultationView.as_view(), name='diagnose_list'),
    path('<int:patient_pk>/diagnose/<int:pk>/', views.DetailConsultationView.as_view(), name='diagnose_detail'),
    path('<int:patient_pk>/diagnose/<int:pk>/update/', views.UpdateConsultationView.as_view(), name='diagnose_edit'),
    path('<int:patient_pk>/diagnose/<int:pk>/delete/', views.DeleteConsultationView.as_view(), name='diagnose_delete'),

    path('<int:patient_pk>/diagnose/<int:pk>/billing/', views.CreateBillingView.as_view(), name='billing_create'),


]
