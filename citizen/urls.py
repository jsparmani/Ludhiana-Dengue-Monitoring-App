from django.urls import path
from . import views

app_name = 'citizen'

urlpatterns = [
    path('add-breeding-site/', views.expected_breedingsites_details,
         name='expected_breedingsites_details'),
    path('expected-patient/', views.expected_patient_details,
         name='expected_patient_details'),
]
