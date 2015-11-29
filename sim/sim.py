import random
import sys
import math
import time
import requests
import json
from threading import Thread

NO_OF_DEVICES = 5

def main():
    f = open("lat-log.csv")
    lines = f.readlines()
    device = 1
    while(True):
        if(device > 5):
            device = 1
        t = Thread(target=pingLatAndLong, args=(device,lines,NO_OF_DEVICES))
        t.start()
        time.sleep(10)
        device = device + 1

def pingLatAndLong(i,lines,interval):
    size = len(lines) / interval
    arr = random.sample(range(1,len(lines)),size)
    for index in arr:
        print i," ",lines[index] #id, lat,log
        time.sleep(5)

if __name__ == "__main__":
    main()
