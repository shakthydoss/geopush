import random
import sys
import math
import thread
import time
import requests
import json
devices = []

def report(device_mac,lat, lon):
    data = {
            "device_mac":device_mac.strip(),
            "location":{
                "lat":lat.strip(),
                "lon":lon.strip()
                }
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    requests.post('http://localhost:5000/ping', data=json.dumps(data), headers=headers)
    print device_mac, lat, lon
    time.sleep(2)

def load_devices():
    file = open("device_id.txt")
    for line in file:
        devices.append(line.replace("\n",""))
    file.close()

def ping():
    for id in devices:
        lan, lon = generate_lat_lon()
        report(id, lan, lon)

def generate_lat_lon():
    latitude = 13.0827
    longitude = 80.2707
    # Create the bounding box
    #set longitude values - Y values
    minx = 13.060081
    maxx = 13.423684

    #set latitude values - X values
    miny = 79.812927
    maxy = 80.202942
    return "{:10.6f}".format(random.uniform(minx,maxx)), "{:10.6f}".format(random.uniform(miny,maxy))

def generate_alpha_numeric():
    print ''.join(random.choice('0123456789ABCDEF') for i in range(16))

if __name__ == "__main__":
    load_devices()
    ping()
    #generate_alpha_numeric()
