from ..models import *
from rest_framework import serializers


class EarthquakeDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Earthquake_Data
        fields = ('url', 'title', 'mag', 'detail', 'xtime')

