# https://stackoverflow.com/questions/41860223/converting-kml-into-postgis-django-python
#https://stackoverflow.com/questions/8000033/how-to-process-an-uploaded-kml-file-in-geodjango
# https://docs.djangoproject.com/en/1.11/ref/contrib/gis/tutorial/
# https://docs.djangoproject.com/en/1.11/ref/contrib/gis/gdal/
from django.contrib.gis.gdal.datasource import DataSource
from ..models import *

# After getting getting Kml from user, save to a temporary file.




# map fields to model
def mapToModel(field_dict, layer):
    """
    not implemented yet, AJAX return of customer input
    :param field_dict: Dictionary of fields mapped by the user
    :param layer: layer that is being input into DB
    :return:
    """
    return False

def add_customer():
    c = Customer()
    c.name = "Todd"
    c.email = "tdhagler1@gmail.com"


def manual_add_kml():
    ds = DataSource("selected.kml")
    layer = ds[0]

    customer = Customer.objects.get(name="Todd")
    geos = layer.get_geoms(geos=True)
    for index, i in enumerate(layer):
        asset = UserAsset()
        asset.owner = customer
        asset.lineString = geos[index]
        asset.assetName = i.get('Name')
        asset.min_mag = 2
        asset.min_warn_distance = 200
        asset.save()
        print(i.get('Name'))