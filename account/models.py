from django.db import models
from django.contrib import auth

# Create your models here.


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username


class ClusterUser(models.Model):

    user = models.OneToOneField(
        auth.models.User, related_name='clusterusers', on_delete=models.CASCADE)
    cluster = models.OneToOneField(
        'location.Cluster', related_name='clusteruserscluster', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class HealthUser(models.Model):

    user = models.OneToOneField(
        auth.models.User, related_name='healthusers', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class DCUser(models.Model):

    user = models.OneToOneField(
        auth.models.User, related_name='dcusers', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
