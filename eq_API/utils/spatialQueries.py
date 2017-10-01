from ..models import *
from django.contrib.gis.measure import Distance, D


def affected_pipelines(earthqauke):
    #still needs work. does not calculate distance in a usefull way
    pipelines = UserAsset.objects.filter(lineString__distance_lte=(earthqauke.coords, D(mi=75)))

    return pipelines

