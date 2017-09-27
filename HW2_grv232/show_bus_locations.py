import sys
mtakey=sys.argv[1]
busline=sys.argv[2]
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+ mtakey +\
"&VehicleMonitoringDetailLevel=calls&LineRef="+busline
print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
print('Bus Line : {}'.format(busline))
print ('Number of active buses: {}'.format(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])))
for it in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
    reference=it['MonitoredVehicleJourney']['VehicleRef']
    latitude=it['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude=it['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print('Bus {} is at latitude {} and longitude {}'.format(reference[9:],latitude,longitude))