from django.shortcuts import render, redirect
from . import forms
from dal import autocomplete
from location import models as loc_models
# Create your views here.


def expected_breedingsites_details(request):

    if request.method == 'POST':
        form = forms.ExpectedBreedingSiteNewForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            if form.cleaned_data['area'] != 'Urban Patiala' and form.cleaned_data['area'] != '--------':
                try:
                    data.locality = loc_models.Locality.objects.get(name__iexact = form.cleaned_data['area'])
                    data.save()
                except:
                    return redirect('fault', fault='Server Error')
            elif form.cleaned_data['area'] != '--------':
                try:
                    if form.cleaned_data['locality'] == '--------':
                        return redirect('fault', fault='Server Error')
                    data.locality = loc_models.Locality.objects.get(name__iexact = form.cleaned_data['locality'])
                    data.save()
                except:
                    return redirect('fault', fault='Server Error')
            else:
                return redirect('fault', fault='Server Error')
            return redirect('view_info_page', uid=4)
        else:
            return redirect('fault', fault="Server Error!")
    else:
        form = forms.ExpectedBreedingSiteNewForm()
        return render(request, 'citizen/expected_breedingsite_details.html', {'form': form})


def expected_patient_details(request):

    if request.method == 'POST':
        form = forms.ExpectedPatientNewForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            if form.cleaned_data['area'] != 'Urban Patiala' and form.cleaned_data['area'] != '--------':
                try:
                    data.locality = loc_models.Locality.objects.get(name__iexact = form.cleaned_data['area'])
                    data.save()
                except:
                    return redirect('fault', fault='Server Error')
            elif form.cleaned_data['area'] != '--------':
                try:
                    if form.cleaned_data['locality'] == '--------':
                        return redirect('fault', fault='Server Error')
                    data.locality = loc_models.Locality.objects.get(name__iexact = form.cleaned_data['locality'])
                    data.save()
                except:
                    return redirect('fault', fault='Server Error')
            else:
                return redirect('fault', fault='Server Error')
            return redirect('map')
        else:
            return redirect('fault', fault="Server Error!")
    else:
        form = forms.ExpectedPatientNewForm()
        return render(request, 'citizen/expected_patient_details.html', {'form': form})
