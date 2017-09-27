from __future__ import print_function
import json
import urllib2 
import os
import sys

apikey = sys.argv[1]
mode = "Json"
busline = sys.argv[2]

# create url using input api and bus line number
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + apikey + \
"&VehicleMonitoringDetailLevel=calls&LineRef=" + busline

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")

# use the json.loads method to obtain a dictionary representation of the response string 
dataDict = json.loads(data)

# count instances of monitored vehicle journey that represent each bus
busNum = len(dataDict["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])

# prints the bus line and number
print("Bus Line : ", busline, "\nNumber of Active Buses : ", busNum)

# isolate monitored vehicle journey
vehicles = dataDict["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

# isolate each vehicle location and seperate out lat and long
for i in range(busNum):
    latitude = str(vehicles[i]["MonitoredVehicleJourney"]["VehicleLocation"]['Latitude'])
    longitude = str(vehicles[i]["MonitoredVehicleJourney"]["VehicleLocation"]['Longitude'])
    print("Bus ", i, "is at latitude ", latitude, "and longitude ", longitude)

 