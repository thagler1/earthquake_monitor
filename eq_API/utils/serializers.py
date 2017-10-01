# https://stackoverflow.com/questions/38218996/how-can-i-get-a-django-rest-framework-with-a-sub-query-on-child-related-items-wo
from ..models import *
from rest_framework import serializers
from django.contrib.gis.measure import Distance, D


class AffectedPipelineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAsset
        fields = ['assetName',]


class Earthquakepipelineserializer(serializers.HyperlinkedModelSerializer):

    pipes = serializers.SerializerMethodField()

    class Meta:
        model = Earthquake_Data
        fields = ('url', 'title', 'mag','coords', 'detail', 'xtime', 'pipes')

    def get_pipes(self, obj):
        pipelines = UserAsset.objects.filter(lineString__distance_lte=(obj.coords, D(mi=75)))
        serializer = AffectedPipelineSerializer(pipelines)
        return serializer.data

class EarthquakeDataSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Earthquake_Data
        fields = ('url', 'title', 'mag', 'detail', 'xtime')
