# https://stackoverflow.com/questions/41860223/converting-kml-into-postgis-django-python
#https://stackoverflow.com/questions/8000033/how-to-process-an-uploaded-kml-file-in-geodjango
# https://docs.djangoproject.com/en/1.11/ref/contrib/gis/tutorial/
# https://docs.djangoproject.com/en/1.11/ref/contrib/gis/gdal/
from django.contrib.gis.gdal.datasource import DataSource
from ..models import *

# After getting getting Kml from user, save to a temporary file.


#load temp file into ds
ds = DataSource("data.kml")
geoms = ds[0].get_geoms(geos=True)

# map fields to model
def mapToModel(field_dict, layer):
    """
    not implemented yet, AJAX return of customer input
    :param field_dict: Dictionary of fields mapped by the user
    :param layer: layer that is being input into DB
    :return:
    """
    return False

