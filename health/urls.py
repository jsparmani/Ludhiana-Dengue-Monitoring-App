from django.urls import path
from . import views

app_name = 'health'

urlpatterns = [
    path('cluster-expected-patients/', views.view_expected_patients_cluster,
         name='view_expected_patients_cluster'),
    path('ward-expected-patients/<int:id>/', views.view_expected_patients_ward,
         name='view_expected_patients_ward'),
    path('locality-expected-patients/<int:id>/', views.view_expected_patients_locality,
         name='view_expected_patients_locality'),
    path('locality-expected-patients-list/<str:name>/', views.view_patients_details,
         name='view_patients_details'),
]
