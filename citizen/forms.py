from django import forms
from . import models
from location import models as loc_models


class ExpectedBreedingSiteForm(forms.ModelForm):

    class Meta:
        model = models.ExpectedBreedingSite
        exclude = ['created_at']


class ExpectedPatientForm(forms.ModelForm):

    class Meta:
        model = models.ExpectedPatient
        exclude = ['created_at']
