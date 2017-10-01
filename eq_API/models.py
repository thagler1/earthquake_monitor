from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
import datetime


# Create your models here.


class Earthquake_Data(models.Model):
    alert = models.CharField(max_length=20, null=True)
    cdi = models.FloatField(default=None, null=True)
    code = models.CharField(max_length=15, default=None, null=True)
    detail = models.URLField( default=None, null=True)
    dmin = models.FloatField(default=None, null=True)
    felt = models.IntegerField(null=True, default=None)
    gap = models.FloatField(null=True, default=None)
    mag = models.FloatField(null=True, default=None)
    magType = models.CharField(max_length=3, default=None, null=True)
    mmi = models.FloatField(null=True, default=None)
    net = models.CharField(max_length=50, null=True, default=None)
    nst = models.IntegerField(null=True, default=None)
    place = models.CharField(max_length=180, default=None, null=True)
    rms = models.FloatField(null=True, default=None)
    sig = models.IntegerField(null=True, default=None)
    sources = models.CharField(max_length=180, default=None, null=True)
    status = models.CharField(max_length=20, default=None, null=True)
    xtime = models.DateTimeField(null=True, default=None)
    title = models.CharField(max_length=180, default=None, null=True)
    tsunami = models.IntegerField(null=True, default=None)
    type = models.CharField(max_length=180, default=None, null=True)
    types = models.CharField(max_length=180, default=None, null=True)
    tz = models.IntegerField(null=True, default=None)
    xupdated = models.DateTimeField(null=True, default=None)
    url= models.URLField(null=True, default=None)
    id = models.CharField(max_length=15, primary_key=True, unique=True)
    coords = models.PointField(default=None, null=True)
    objects = models.GeoManager()


    def __str__(self):
        return self.title

    def import_data(self, element):
        # used for import Json data to class

        temp = {}

        for k, v in element['properties'].items():
            if k in dir(self):
                try:
                    setattr(self, k, v)
                except Exception as exc:
                    self.k = None
                    print("failed on %s - |" % k)
        self.id = element['id']
        rtime = datetime.datetime.utcfromtimestamp(int(element['properties']['time'])/1000)
        rtime += datetime.timedelta(minutes=self.tz)
        self.xtime = rtime

        self.coords = GEOSGeometry('POINT(%s %s)' % (
            element['geometry']['coordinates'][0],
            element['geometry']['coordinates'][1]), srid=4326)


        #self.xtime = datetime.datetime.strptime(t)
        try:
            self.save()
        except Exception as e:
            print(e)
        return self


    class Asset(models.Model):
        objects = models.GeoManager()

class Customer(models.Model):
    name = models.CharField(max_length=200, default=None)
    email = models.EmailField(default=None)


    def __str__(self):
        return self.name


class UserAsset(models.Model):
    objects = models.GeoManager()
    assetName = models.CharField(max_length=200, default=None, null=True)
    min_mag = models.FloatField(default=1)
    min_warn_distance = models.FloatField(default=10)
    contact_email = models.EmailField(default=None, null=True)
    point = models.PointField(default=None, null=True)
    line = models.LineStringField(default=None, null=True)
    polygon = models.PolygonField(default=None, null=True)
    owner = models.OneToOneField(Customer)

    def __str__(self):
        return self.assetName
