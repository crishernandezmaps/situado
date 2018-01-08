#!/usr/bin/python3
# coding: utf-8
import pandas as pd
from geopy.geocoders import Bing

bing_key = "ginITT5ALcrOnA4aMoH0~_vGQBu-_tnKr6FYRj6U5nA~Ar9conblprRVoeaB4uH4PKMzcs0BfrUJ5LbspSyDn04UqCpCOfsm567DJjUw-PY6" # https://www.bingmapsportal.com/Account
pathToFile = "data/cc.csv"

def lat(row):
    geolocator = Bing(bing_key, timeout=5)
    location = geolocator.geocode(row['Address'])
    return str(location.latitude)

def lon(row):
    geolocator = Bing(bing_key, timeout=5)
    location = geolocator.geocode(row['Address'])
    return str(location.longitude)

df = pd.read_csv(pathToFile,sep=',')
df['lat'] = df.apply(lambda row: lat(row),axis=1)
df['lon'] = df.apply(lambda row: lon(row),axis=1)
df.to_csv('data/cc_coor.csv',sep=',')
print(df)
