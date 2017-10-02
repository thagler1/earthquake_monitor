from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .utils.serializers import EarthquakeDataSerializer, Earthquakepipelineserializer
from .models import *
import datetime
from .usgs.eq_import import import_data
from django.http import HttpResponse

class EarthQuakeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that shows all seismic events in the database.
    """
    queryset = Earthquake_Data.objects.all()
    serializer_class = EarthquakeDataSerializer


class LastHour(viewsets.ModelViewSet):
    """
    API endpoint that shows earthquakes in the last hour
    """
    queryset = Earthquake_Data.objects.filter(xtime__gte = datetime.datetime.utcnow() - datetime.timedelta(hours=1))
    serializer_class = EarthquakeDataSerializer

class LasthourPipelines(viewsets.ModelViewSet):
    """
    API endpoint that shows pipeline affected by earthquakes in the last hour
    currently shows all pipelines
    """
    queryset = Earthquake_Data.objects.filter(xtime__gte = datetime.datetime.utcnow() - datetime.timedelta(hours=1))
    serializer_class = Earthquakepipelineserializer

def manual_update(request):
    import_data()
    return HttpResponse("Updated")

