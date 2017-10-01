from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .utils.serializers import EarthquakeDataSerializer
from .models import *
import datetime
from .usgs.eq_import import import_data
from django.http import HttpResponse

class EarthQuakeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Earthquake_Data.objects.all()
    serializer_class = EarthquakeDataSerializer


class LastHour(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Earthquake_Data.objects.filter(xtime__gte = datetime.datetime.utcnow() - datetime.timedelta(hours=1))
    serializer_class = EarthquakeDataSerializer

def manual_update(request):
    import_data()
    return HttpResponse("Updated")

