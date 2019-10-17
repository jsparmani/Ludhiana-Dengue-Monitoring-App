from django.shortcuts import render, redirect
from citizen import models as cit_models
from location import models as loc_models
from django.contrib.auth.decorators import login_required
import json


@login_required
def view_expected_patients_cluster(request):
    clusters = loc_models.Cluster.objects.all()
    cluster_details = []
    sites_count = {}
    label = 'Expected Dengue Patients'
    data_series = [u['cluster_id'] for u in clusters.values('cluster_id')]
    data_series = [str(x) for x in data_series]

    data = []
    for cluster in clusters:
        count = cit_models.ExpectedPatient.objects.all().filter(
            locality__ward__cluster=cluster).count()
        sites_count[cluster.cluster_id] = [cluster.lat, cluster.lng, count]

        data.append(count)

    data_dict = {'name': label, 'data': data}
    jsondata = {'data_series': data_series, 'data_dict': [data_dict]}

    jsondata = json.dumps(jsondata)

    return render(request, 'health/view_expected_patients_cluster.html', {'sites_count': sites_count, 'jsondata': jsondata})


@login_required
def view_expected_patients_ward(request, id):
    wards = loc_models.Ward.objects.all().filter(cluster__cluster_id__exact=id)
    sites_count = {}
    label = 'Expected Breeding Sites'
    data_series = [u['ward_id'] for u in wards.values('ward_id')]
    data_series = [str(x) for x in data_series]
    data = []
    for ward in wards:
        count = cit_models.ExpectedPatient.objects.all().filter(
            locality__ward=ward).count()
        sites_count[ward.ward_id] = [ward.lat, ward.lng, count]
        data.append(count)

    data_dict = {'name': label, 'data': data}
    jsondata = {'data_series': data_series, 'data_dict': [data_dict]}

    jsondata = json.dumps(jsondata)
    return render(request, 'health/view_expected_patients_ward.html', {'sites_count': sites_count, 'jsondata': jsondata})


@login_required
def view_expected_patients_locality(request, id):
    localities = loc_models.Locality.objects.all().filter(ward__ward_id__exact=id)
    sites_count = {}
    label = 'Expected Breeding Sites'
    data_series = [u['name'] for u in localities.values('name')]
    data_series = [str(x) for x in data_series]
    data = []
    for locality in localities:
        count = cit_models.ExpectedPatient.objects.all().filter(
            locality=locality).count()
        sites_count[locality.name] = [locality.lat, locality.lng, count]
        data.append(count)

    data_dict = {'name': label, 'data': data}
    jsondata = {'data_series': data_series, 'data_dict': [data_dict]}

    jsondata = json.dumps(jsondata)

    return render(request, 'health/view_expected_patients_locality.html', {'sites_count': sites_count, 'jsondata': jsondata})


@login_required
def view_patients_details(request, name):
    patients = cit_models.ExpectedPatient.objects.all().filter(
        locality__name__exact=name)
    return render(request, 'health/view_expected_patient_complaints.html', {'patients': patients})
