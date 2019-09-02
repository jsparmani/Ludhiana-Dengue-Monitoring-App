from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.DCUser)
admin.site.register(models.HealthUser)
admin.site.register(models.ClusterUser)
