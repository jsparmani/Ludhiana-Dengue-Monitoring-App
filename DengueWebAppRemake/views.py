from django.shortcuts import render, redirect
from location import models as loc_models
from django.http import HttpResponse
import googlemaps
from account import models as acc_models
from django.contrib.auth.models import User

gmaps = googlemaps.Client(key='AIzaSyBfdLxVxC4rR_Cz-NumqwcjqWgbVZ98ZEs')


def home(request):
    return render(request, 'home.html')


def fault(request, fault):
    return render(request, 'fault.html', {'fault': fault})


def info(request):
    return render(request, 'info.html')


def view_info_page(request, uid):

    if uid == 1:
        return render(request, 'DosAndDonts.html')
    elif uid == 2:
        return render(request, 'faq.html')
    elif uid == 3:
        return render(request, 'aedesmosquito.html')
    elif uid == 4:
        return render(request, 'prevention.html')
    elif uid == 5:
        return render(request, 'signandsymptoms.html')
    elif uid == 6:
        return render(request, 'tests.html')
    elif uid == 7:
        return render(request, 'myths.html')
    elif uid == 8:
        return render(request, 'dryday.html')
    elif uid == 9:
        return render(request, 'message.html')
    elif uid == 10:
        return render(request, 'symptoms.html')


def map(request):
    return render(request, 'map.html')


def populate_ward(request):
    cluster = 4
    wards = [x for x in range(28, 36)]
    for w in wards:
        loc_models.Ward.objects.create(
            cluster=loc_models.Cluster.objects.get(cluster_id__exact=cluster),
            ward_id=w,
            lat=0,
            lng=0
        )

    cluster = 5
    wards = [x for x in range(36, 44)]
    for w in wards:
        loc_models.Ward.objects.create(
            cluster=loc_models.Cluster.objects.get(cluster_id__exact=cluster),
            ward_id=w,
            lat=0,
            lng=0
        )

    cluster = 6
    wards = [x for x in range(44, 53)]
    for w in wards:
        loc_models.Ward.objects.create(
            cluster=loc_models.Cluster.objects.get(cluster_id__exact=cluster),
            ward_id=w,
            lat=0,
            lng=0
        )

    cluster = 7
    wards = [x for x in range(53, 61)]
    for w in wards:
        loc_models.Ward.objects.create(
            cluster=loc_models.Cluster.objects.get(cluster_id__exact=cluster),
            ward_id=w,
            lat=0,
            lng=0
        )
    return HttpResponse("done")


def populate_locality(request):
    f1 = open(
        'D:\Codes\Django\LDMA\Ludhiana-Dengue-Monitoring-App\loc.txt', 'r')

    f2 = open('D:\Codes\Django\LDMA\Ludhiana-Dengue-Monitoring-App\loc_not.txt', 'a')

    a = f1.read().split('\n')

    b = []
    # for item in a:
    #     b.append(item.split(','))
    execute = 0
    count_test = 248
    for c in a:
        try:
            geocode_result = gmaps.geocode(f'{c}, Ludhiana, Punjab')
            lat = geocode_result[0]['geometry']['location']['lat']
            lng = geocode_result[0]['geometry']['location']['lng']

        except:
            f2.write(c+'\n')
            continue

        loc_models.Locality.objects.create(
            ward=loc_models.Ward.objects.get(ward_id__exact=28),
            loc_id=count_test,
            name=c,
            lat=lat,
            lng=lng

        )

        count_test += 1
        execute += 1

        for x in range(1000):
            pass

    return HttpResponse(f'Badhiya {execute}')


def populate_ward_latlng(request):

    wards = loc_models.Ward.objects.all()

    for ward in wards:
        lat = lng = 0
        localities = ward.localities.all()
        for locality in localities:
            lat += float(locality.lat)
            lng += float(locality.lng)

        if len(localities):
            lat = lat/len(localities)
            lng = lng/len(localities)
        else:
            lat = lng = 0

        ward.lat = lat
        ward.lng = lng
        ward.save()

    return HttpResponse("Done")


def populate_cluster_latlng(request):

    clusters = loc_models.Cluster.objects.all()

    for cluster in clusters:
        lat = lng = 0
        wards = cluster.wards.all()
        for ward in wards:
            lat += float(ward.lat)
            lng += float(ward.lng)

        if len(wards):
            lat = lat/len(wards)
            lng = lng/len(wards)
        else:
            lat = lng = 0

        cluster.lat = lat
        cluster.lng = lng
        cluster.save()

    return HttpResponse("Done")


def create_cluster_users(request):
    for i in range(1, 29):
        user = User.objects.create(
            username=f'cluster{i}',
            password='denguefree'
        )

        san_name = ['Sh. Gurdial Singh', 'Sh. Gurdial Singh', 'Kulbir Singh', 'Pritpal Singh', 'Amit Shai', 'Jagjit Singh', 'Manjit Singh', 'Pankaj Patti', 'Gurwinder Singh', 'Sh. Gurwinder Singh', 'Amrit Pal Singh', 'Gurpreet Singh', 'Gurpreet Singh',
                    'Aamrit Pal Singh', 'Gurpreet Singh', 'Sarbjit Singh', 'Sarbjit Singh', 'Amit Sahi', 'Varinder Mohan', 'Gurdev Singh', 'Gurdev Singh', 'Gurminder Singh', 'Manmohan Singh', 'Mohan Singh', 'Parminder Singh', 'Sukhminder Singh', 'Karam Singh', 'Kulwant Singh']

        c_m = loc_models.Cluster.objects.create(
            cluster_id=i,
            sanitary_inspector_name=san_name[i-1],
            sanitary_inspector_phone=0,
            sanitary_inspector_email='hello@gmail.com',
            lat='70',
            lng='70'
        )

        user.set_password('denguefree')
        user.save()

        acc_models.ClusterUser.objects.create(
            user=user,
            cluster=c_m
        )

        loc_models.Ward.objects.create(
            cluster=c_m,
            ward_id=i,
            lat='70',
            lng='70'
        )

    return HttpResponse("done")
