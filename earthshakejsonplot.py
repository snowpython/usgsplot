import json
import urllib.request
from geopy.distance import geodesic
import matplotlib.pyplot as plt
from datetime import datetime
import mplcursors

webUrl = urllib.request.urlopen('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson')
data = json.loads(webUrl.read())
quakes = []
quakex = []
quakey = []
quakez = []
labels = []
distanceFromEarthquake = 17
for i in data['features']:
    firstEarthquake = (40.751, -112.078)
    second = (i['geometry']['coordinates'][1],i['geometry']['coordinates'][0])
    if geodesic(firstEarthquake,second).miles < distanceFromEarthquake:
        labelAppend = f"Magnitude: {i['properties']['mag']}"
        labelAppend = labelAppend + f'\n Date: {datetime.fromtimestamp(i["properties"]["time"]/1000.0).strftime("%m/%d/%Y, %H:%M:%S")}'
        labelAppend = labelAppend + f"\n Depth: {i['geometry']['coordinates'][2]}"
        labels.append(labelAppend)
        quakex.append(datetime.fromtimestamp(i['properties']['time']/1000.0))
        quakey.append(i['geometry']['coordinates'][2])
        quakez.append(i['properties']['mag']*10)
        quakes.append(i)

plt.scatter(quakex,quakey,s=quakez)
plt.ylabel('Depth')
plt.xlabel('Time')
mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(labels[sel.target.index]))
plt.show()
