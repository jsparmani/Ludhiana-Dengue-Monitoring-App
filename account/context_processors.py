from .import models


def UserList(request):
    cluster_all = [u['user']
                   for u in models.ClusterUser.objects.all().values('user')]
    health_all = [u['user']
                  for u in models.HealthUser.objects.all().values('user')]
    dc_all = [u['user'] for u in models.DCUser.objects.all().values('user')]

    return {'cluster_all': cluster_all, 'health_all': health_all, 'dc_all': dc_all}
