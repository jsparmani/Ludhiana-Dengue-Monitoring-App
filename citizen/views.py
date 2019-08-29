from django.shortcuts import render, redirect
from . import forms
from dal import autocomplete
from location import models as loc_models
# Create your views here.


def expected_breedingsites_details(request):

    if request.method == 'POST':
        form = forms.ExpectedBreedingSiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('fault', fault="Server Error!")
    else:
        form = forms.ExpectedBreedingSiteForm()
        return render(request, 'citizen/expected_breedingsite_details.html', {'form': form})


def expected_patient_details(request):

    if request.method == 'POST':
        form = forms.ExpectedPatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('fault', fault="Server Error!")
    else:
        form = forms.ExpectedPatientForm()
        return render(request, 'citizen/expected_patient_details.html', {'form': form})
