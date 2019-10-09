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


class ExpectedBreedingSiteNewForm(forms.ModelForm):

    other_localities = [
        ('Urban Patiala', 'Urban Patiala'),
        ('Rajpura', 'Rajpura'),
        ('Nabha', 'Nabha'),
        ('Samana', 'Samana'),
        ('Sanaur', 'Sanaur'),
        ('Patran', 'Patran'),
        ('Ghagga', 'Ghagga'),
        ('Ghanaur', 'Ghanaur'),
        ('Bhadson', 'Bhadson'),
    ]

    localities = [u['name'] for u in loc_models.Locality.objects.all().values('name')]
    localities = [(x,x) for x in localities]

    localities = list(set(localities)-set(other_localities))
    localities.sort()
    localities = [('--------','--------')] + localities

    other_localities = [('--------','--------')] + other_localities

    area = forms.ChoiceField(choices=other_localities)
    locality = forms.ChoiceField(choices=localities, widget=forms.Select(attrs={'class':'loc'}))

    class Meta:
        model = models.ExpectedBreedingSite
        exclude = ['created_at', 'locality']

    def __init__(self, *args, **kwargs):
        super(ExpectedBreedingSiteNewForm, self).__init__(*args, **kwargs)
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


class ExpectedPatientNewForm(forms.ModelForm):

    other_localities = [
            ('Urban Patiala', 'Urban Patiala'),
            ('Rajpura', 'Rajpura'),
            ('Nabha', 'Nabha'),
            ('Samana', 'Samana'),
            ('Sanaur', 'Sanaur'),
            ('Patran', 'Patran'),
            ('Ghagga', 'Ghagga'),
            ('Ghanaur', 'Ghanaur'),
            ('Bhadson', 'Bhadson'),
        ]

    localities = [u['name'] for u in loc_models.Locality.objects.all().values('name')]
    localities = [(x,x) for x in localities]

    localities = list(set(localities)-set(other_localities))
    localities.sort()
    localities = [('--------','--------')] + localities

    other_localities = [('--------','--------')] + other_localities

    area = forms.ChoiceField(choices=other_localities)
    locality = forms.ChoiceField(choices=localities, widget=forms.Select(attrs={'class':'loc'}))

    class Meta:
        model = models.ExpectedPatient
        exclude = ['created_at', 'locality']

    def __init__(self, *args, **kwargs):
        super(ExpectedPatientNewForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget = forms.Textarea(attrs={
            'class': 'materialize-textarea',
        })
        self.fields['name'].widget = forms.TextInput(attrs={
            'autofocus': 'autofocus'
        })
