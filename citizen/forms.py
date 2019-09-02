from django import forms
from . import models
from location import models as loc_models


class ExpectedBreedingSiteForm(forms.ModelForm):

    class Meta:
        model = models.ExpectedBreedingSite
        exclude = ['created_at']

    def __init__(self, *args, **kwargs):
        super(ExpectedBreedingSiteForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget = forms.Textarea(attrs={
            'class': 'materialize-textarea',
        })
        self.fields['name'].widget = forms.TextInput(attrs={
            'autofocus': 'autofocus'
        })


class ExpectedPatientForm(forms.ModelForm):

    class Meta:
        model = models.ExpectedPatient
        exclude = ['created_at']

    def __init__(self, *args, **kwargs):
        super(ExpectedPatientForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget = forms.Textarea(attrs={
            'class': 'materialize-textarea',
        })
        self.fields['name'].widget = forms.TextInput(attrs={
            'autofocus': 'autofocus'
        })
