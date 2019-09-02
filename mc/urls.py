from django.urls import path
from . import views

app_name = 'mc'

urlpatterns = [
    path('cluster-expected-breeding/', views.view_expected_breedingsite_cluster,
         name='view_expected_breedingsite_cluster'),
    path('ward-expected-breeding/<int:id>/', views.view_breedingsites_ward,
         name='view_breedingsites_ward'),
    path('locality-expected-breeding/<int:id>/', views.view_breedingsites_locality,
         name='view_breedingsites_locality'),
    path('locality-expected-breeding-complaints/<str:name>/', views.view_breedingsites_complaint,
         name='view_breedingsites_complaint'),
]
