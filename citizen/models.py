from django.db import models

# Create your models here.


class ExpectedBreedingSite(models.Model):
    name = models.CharField(max_length=50, blank=False)
    phone = models.PositiveIntegerField(blank=False)
    address = models.TextField(blank=False)
    locality = models.ForeignKey(
        'location.Locality', related_name='expectedbreedingsites', on_delete=models.CASCADE, blank=False)
    image = models.ImageField(upload_to='images/breeding-sites', blank=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['name', 'phone', 'locality']
        ordering = ['-pk']

    def __str__(self):
        return f'{self.locality} {self.name}'


class ExpectedPatient(models.Model):

    name = models.CharField(max_length=50, blank=False)
    phone = models.PositiveIntegerField(blank=False)
    address = models.TextField(blank=False)
    locality = models.ForeignKey(
        'location.Locality', related_name='expectedpatients', on_delete=models.CASCADE, blank=False)
    a1 = models.BooleanField(default=False, blank=False)
    a2 = models.BooleanField(default=False, blank=False)
    a3 = models.BooleanField(default=False, blank=False)
    a4 = models.BooleanField(default=False, blank=False)
    a5 = models.BooleanField(default=False, blank=False)
    a6 = models.BooleanField(default=False, blank=False)
    a7 = models.BooleanField(default=False, blank=False)
    a8 = models.BooleanField(default=False, blank=False)

    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['name', 'phone', 'locality']
        ordering = ['-pk']

    def __str__(self):
        return self.name
