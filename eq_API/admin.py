from .models import *
from django.contrib import admin
from django.contrib.gis import admin
admin.site.register(Earthquake_Data, admin.GeoModelAdmin)
