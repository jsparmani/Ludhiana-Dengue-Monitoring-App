from django.shortcuts import render, redirect
from citizen import models as cit_models
from location import models as loc_models


def view_expected_breedingsite_cluster(request):
    clusters = loc_models.Cluster.objects.all()
    cluster_details = []
    sites_count = {}
    for cluster in clusters:
        count = cit_models.ExpectedBreedingSite.objects.all().filter(
            locality__ward__cluster=cluster).count()
        sites_count[cluster.cluster_id] = [cluster.lat, cluster.lng, count]
    return render(request, 'mc/view_expected_breedingsite_cluster.html', {'sites_count': sites_count})


def view_breedingsites_ward(request, id):
    wards = loc_models.Ward.objects.all().filter(cluster__cluster_id__exact=id)
    sites_count = {}
    for ward in wards:
        count = cit_models.ExpectedBreedingSite.objects.all().filter(
            locality__ward=ward).count()
        sites_count[ward.ward_id] = count
    return render(request, 'mc/view_expected_breedingsite_ward.html', {'sites_count': sites_count})


def view_breedingsites_locality(request, id):
    localities = loc_models.Locality.objects.all().filter(ward__ward_id__exact=id)
    sites_count = {}
    for locality in localities:
        count = cit_models.ExpectedBreedingSite.objects.all().filter(
            locality=locality).count()
        sites_count[locality.name] = count
    return render(request, 'mc/view_expected_breedingsite_locality.html', {'sites_count': sites_count})
