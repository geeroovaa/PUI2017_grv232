import sys
import os
import pandas as pd
mtakey=sys.argv[1]
busline=sys.argv[2]
filename=sys.argv[3]
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
df=[]
for i in range (0,len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])):
    latitude=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    try:
        status=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        name=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    except KeyError:
        status='N/A'
        name='N/A'
    df.append([latitude,longitude,name,status])
df=pd.DataFrame(df,columns=['Latitude','Longitude','Stop Name','Stop Status'])
df.to_csv(filename,index=False)
