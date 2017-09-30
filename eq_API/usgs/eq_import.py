# Utility for getting new data from USGS
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
import requests
import json
from ..models import Earthquake_Data

def import_data():
    response = requests.get(r"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson")
    data = json.loads(response.text)
    for q in data['features']:
        if q['properties']['type'] == "earthquake":
            if Earthquake_Data.objects.filter(id=q['id']).exists():
                try:
                    x = Earthquake_Data()
                    x.import_data(q)



                except Exception as e:
                    print("Failed to create %s" % q['id'])
                    print(e)





