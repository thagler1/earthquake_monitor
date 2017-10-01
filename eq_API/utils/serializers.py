# https://stackoverflow.com/questions/38218996/how-can-i-get-a-django-rest-framework-with-a-sub-query-on-child-related-items-wo
from ..models import *
from rest_framework import serializers


class AffectedPipelineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAsset
        fields = ('assetName')


class Earthquakepipelineserializer(serializers.HyperlinkedModelSerializer):

    pipes = serializers.SerializerMethodField()

    class Meta:
        model = Earthquake_Data
        fields = ('url', 'title', 'mag', 'detail', 'xtime', 'pipes')

        def get_pipes(self, obj):
            pipelines = UserAsset.objects.filter(lineString__distance_lte=(self.coords, D(mi=75)))
            serializer = AffectedPipelineSerializer(pipelines, many=True)
            return serializer.data

class EarthquakeDataSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Earthquake_Data
        fields = ('url', 'title', 'mag', 'detail', 'xtime')
