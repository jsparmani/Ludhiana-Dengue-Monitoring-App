"""DengueWebAppRemake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('map/', views.map, name='map'),
    path('', include('pwa.urls')),
    path('info/', views.info, name='info'),
    path('info-page/<int:uid>/', views.view_info_page, name='view_info_page'),
    path('fault/<str:fault>/', views.fault, name='fault'),
    path('account/', include('account.urls')),
    path('location/', include('location.urls')),
    path('citizen/', include('citizen.urls')),
    path('health/', include('health.urls')),
    path('mc/', include('mc.urls')),
    path('populate_ward/', views.populate_ward),
    path('populate_locality/', views.populate_locality),
    path('populate_ward_latlng/', views.populate_ward_latlng),
    path('populate_cluster_latlng/', views.populate_cluster_latlng),
    path('create_cluster_users/', views.create_cluster_users),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
