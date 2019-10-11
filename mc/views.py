from django.shortcuts import render, redirect
from citizen import models as cit_models
from location import models as loc_models
from account import models as acc_models
from django.contrib.auth.decorators import login_required
import json


@login_required
def view_expected_breedingsite_cluster(request):
    named_clusters = ['Rajpura','Nabha','Samana','Sanaur','Patran','Ghagga','Ghanaur','Bhadson']
    if request.user.username in ['healthpatiala','dcpatiala']:
        clusters = loc_models.Cluster.objects.all()
    else:
        clusters = loc_models.Cluster.objects.all().filter(pk__exact=acc_models.ClusterUser.objects.get(
            user__username__exact=request.user.username).cluster.pk)
    cluster_details = []
    sites_count = {}
    label = 'Expected Breeding Sites'
    data_series = [u['cluster_id'] for u in clusters.values('cluster_id')]
    data_series = [str(x) for x in data_series]
    data_series = data_series[0:7]
    data_series.extend(named_clusters)
    data = []
    for cluster in clusters:
        count = cit_models.ExpectedBreedingSite.objects.all().filter(
            locality__ward__cluster=cluster).count()
        sites_count[cluster.cluster_id] = [cluster.lat, cluster.lng, count]

        data.append(count)

    data_dict = {'name': label, 'data': data}
    jsondata = {'data_series': data_series, 'data_dict': [data_dict]}

    jsondata = json.dumps(jsondata)

    return render(request, 'mc/view_expected_breedingsite_cluster.html', {'sites_count': sites_count, 'jsondata': jsondata})


@login_required
def view_breedingsites_ward(request, id):
    wards = loc_models.Ward.objects.all().filter(cluster__cluster_id__exact=id)

    sites_count = {}
    label = 'Expected Breeding Sites'
    data_series = [u['ward_id'] for u in wards.values('ward_id')]
    data_series = [str(x) for x in data_series]
    data = []
    for ward in wards:
        count = cit_models.ExpectedBreedingSite.objects.all().filter(
            locality__ward=ward).count()
        sites_count[ward.ward_id] = [ward.lat, ward.lng, count]

        data.append(count)

    data_dict = {'name': label, 'data': data}
    jsondata = {'data_series': data_series, 'data_dict': [data_dict]}

    jsondata = json.dumps(jsondata)

    return render(request, 'mc/view_expected_breedingsite_ward.html', {'sites_count': sites_count, 'jsondata': jsondata})


@login_required
def view_breedingsites_locality(request, id):
    localities = loc_models.Locality.objects.all().filter(ward__ward_id__exact=id)
    sites_count = {}
    label = 'Expected Breeding Sites'
    data_series = [u['name'] for u in localities.values('name')]
    data_series = [str(x) for x in data_series]
    data = []
    for locality in localities:
        count = cit_models.ExpectedBreedingSite.objects.all().filter(
            locality=locality).count()
        sites_count[locality.name] = [locality.lat, locality.lng, count]

        data.append(count)

    data_dict = {'name': label, 'data': data}
    jsondata = {'data_series': data_series, 'data_dict': [data_dict]}

    jsondata = json.dumps(jsondata)

    return render(request, 'mc/view_expected_breedingsite_locality.html', {'sites_count': sites_count, 'jsondata': jsondata})


@login_required
def view_breedingsites_complaint(request, name):
    breedingsites = cit_models.ExpectedBreedingSite.objects.all().filter(
        locality__name__exact=name)
    return render(request, 'mc/view_expected_breedingsite_complaints.html', {'breedingsites': breedingsites})
