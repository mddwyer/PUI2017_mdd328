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

#use the json.loads method to obtain a dictionary representation of the reponse string 
dataDict = json.loads(data)

# count instances of monitored vehicle journey that represent each bus
busNum = len(dataDict["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])

# isolate monitored vehicle journey
vehicles = dataDict["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

# open a file for writing
fout = open(sys.argv[3], "w")

fout.write("Latitude,Longitude,Stop Name,Stop Status \n")

# finds variables within the json given a specific vehicle number
for i in range(busNum):
    latitude = str(vehicles[i]["MonitoredVehicleJourney"]["VehicleLocation"]['Latitude'])
    longitude = str(vehicles[i]["MonitoredVehicleJourney"]["VehicleLocation"]['Longitude'])
    stopName = vehicles[i]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
    stopStatus = (vehicles[i]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"])
    if len(stopStatus) == 0:
        stopStatus = "N'A"
    elif len(stopName) == 0:
        stopName = "N/A"
    fout.write(latitude + "," + longitude + "," + stopName + "," + stopStatus + "\n")


