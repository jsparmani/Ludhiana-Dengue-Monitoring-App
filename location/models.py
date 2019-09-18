from django.db import models

# Create your models here.


class Cluster(models.Model):
    cluster_id = models.PositiveIntegerField(blank=False)
    sanitary_inspector_name = models.CharField(max_length=50, blank=False)
    sanitary_inspector_phone = models.PositiveIntegerField(blank=False)
    sanitary_inspector_email = models.EmailField()
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.cluster_id}'


class Ward(models.Model):
    cluster = models.ForeignKey(
        'location.Cluster', related_name='wards', on_delete=models.CASCADE)
    ward_id = models.PositiveIntegerField(blank=False)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.ward_id}'


class Locality(models.Model):
    ward = models.ForeignKey(
        'location.Ward', related_name='localities', on_delete=models.CASCADE)
    loc_id = models.PositiveIntegerField(blank=False)
    name = models.CharField(max_length=50, blank=False)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'
