# -*- coding: utf-8 -*-


import os

# connect to the API
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date

USER = os.environ['DHUS_USER']
PASSWORD = os.environ['DHUS_PASSWORD']
URL = os.environ['DHUS_URL']  # 'https://scihub.copernicus.eu/dhus'


api = SentinelAPI(USER, PASSWORD, URL)


footprint = geojson_to_wkt(read_geojson('map.geojson'))
products = api.query(footprint,
                     producttype='SLC',
                     orbitdirection='ASCENDING')
api.download_all(products)
