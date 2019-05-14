# FireFromSpace

_Detect fire from satellite images_ 

Be it forest fires or villages being attacked, some fires can be detected from space. We hope to build a tool for monitoring the environment and watching for the safety of defenseless civilians.


## Content

* [Goal](#goal)
* [What Are We Doing?](#what-are-we-doing)
* [Join The Project](#join-the-project)
    * [We Need Your Help](#we-need-your-help)
* [More Information](#more-information)
    * [Spotted fires from space](#spotted-fires-from-space)
    * [About Sentinel2](#about-sentinel2)
    * [References](#references)
* [Tools](#tools)
    * [Visualize satellite images online](#visualize-satellite-images-online)
    * [Image processing tools](#image-processing-tools)
    * [Archves of satellites images](#archves-of-satellites-images)
    * [Platforms/APIs for downloading satellite data](#platformsapis-for-downloading-satellite-data)
* [Installation](#installation)
* [Thanks](#thanks)


## Goal

Our goals is to help monitor fires all over the globe for plenty of good reasons.


## What Are We Doing?

While many satellite's images are [free to access](https://apps.sentinel-hub.com/sentinel-playground), the amount of images to process in order to watch the whole of earth is just too big (over 4 Terabytes of fresh products published every day on the Copernicus portals).

This tool won't allow us to monitor the entire planet. But it will be the bsis of an opensource webapp for anyone to use, giving everyone the possibility to monitor a part of earth for large fires  (e.g. fire of a dry forest, garbage burning illegally intoxicating its neighbours, or a tool for the United Nations to watch for genocide and human rights atrocities.

This project is mainly split into 2 applications:

- **a python library for handling Satellite's images and processing them to detect fire**: to measure and to locate the fire as accurately as possible. This module should be easily usable by any developer with a computer, therefore without worrying about any cost of cloud resources.

- **a webapp for non-developers eager to get alerted in case of fires**: For the other users who prefer a user interface, a webapp should allow them to rent cloud resources required for monitoring the part of earth they are interested in, or to share the cost with others watching the same area already.


## Join The Project

Join us on [Slack](http://dataforgood.no/contact-us/), then join our [channel](https://dataforgood-norway.slack.com/messages/CFJFRAKT2/).


### We Need Your Help

See [all tasks](https://github.com/DataForGood-Norway/FireFromSpace/issues?q=is%3Aopen) organised in:

* [Milestones/Objectives](https://github.com/DataForGood-Norway/FireFromSpace/milestones),
* [Kanban boards](https://github.com/DataForGood-Norway/FireFromSpace/projects) to track their development.

The project is just starting, but come help us or learn with us. Don't hesitate to contact us and ask questions on [our Slack channel](https://dataforgood-norway.slack.com/messages/CFJFRAKT2/).



## More Information

### Spotted fires from space

- Wildfires in California, USA clearly visile on [Sentinel Hub](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=36.22004146127195&lng=-118.61878395080566&zoom=13&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=30&gain=1.0&gamma=1.0&time=2018-05-01%7C2018-11-08&atmFilter=&showDates=true), less visible on [planet.com](https://www.planet.com/explorer/#/types/Sentinel2L1C/mosaic/global_monthly_2017_11_mosaic/center/-118.687,36.204/zoom/12/dates/2018-12-08T11:00:00.000Z..2018-12-19T23:59:59.999Z/geometry/POLYGON((-118.5289+36.22,-118.5306+36.2341,-118.5357+36.2477,-118.544+36.2602,-118.5552+36.2712,-118.5688+36.2802,-118.5844+36.2869,-118.6012+36.291,-118.6187+36.2924,-118.6363+36.291,-118.6531+36.2869,-118.6686+36.2802,-118.6823+36.2712,-118.6934+36.2602,-118.7017+36.2477,-118.7068+36.2341,-118.7086+36.22,-118.7068+36.2059,-118.7017+36.1923,-118.6934+36.1797,-118.6823+36.1687,-118.6686+36.1597,-118.6531+36.153,-118.6363+36.1489,-118.6187+36.1475,-118.6012+36.1489,-118.5844+36.153,-118.5688+36.1597,-118.5552+36.1687,-118.544+36.1797,-118.5357+36.1923,-118.5306+36.2059,-118.5289+36.22))/items/Sentinel2L1C%3AS2A_MSIL1C_20181218T184801_N0207_R070_T11SLA_20181218T202646/centerMarker/true/interval/1%20day) (Nov. 8th 2018).
- Spotting Colombia deforestation (before on [2018, Feb. 9th](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=2.161990957069677&lng=-72.38258600234985&zoom=15&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2017-08-01%7C2018-02-09&atmFilter=&showDates=true) and after on [2018, Feb. 10th](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=2.161990957069677&lng=-72.38258600234985&zoom=15&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2017-08-01%7C2018-02-10&atmFilter=&showDates=true), moving on on [2018, Feb 20th](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=2.161990957069677&lng=-72.38258600234985&zoom=15&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2017-08-01%7C2018-02-20&atmFilter=&showDates=true).
- Deonar's garbage burning [(2016, Janv. 30th)](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=19.06994618081784&lng=72.92392015457153&zoom=15&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2015-07-01%7C2016-01-30&atmFilter=&showDates=true),  continuously polluting the air until [2016, March 28th](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=19.06994618081784&lng=72.92392015457153&zoom=15&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2015-09-01%7C2016-03-28&atmFilter=&showDates=true).
- [Southern Portugal, August 2018](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=37.274530905549355&lng=-8.45998764038086&zoom=13&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=39&gain=1.0&gamma=1.0&time=2018-02-01%7C2018-08-08&atmFilter=&showDates=false).
- [Central Portugal, Summer 2017](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=39.98843197151454&lng=-8.052978515625&zoom=11&preset=2_COLOR_INFRARED__VEGETATION_&layers=B01,B02,B03&maxcc=100&gain=1.0&gamma=1.0&time=2017-01-01%7C2017-07-07&atmFilter=&showDates=false).
- [La Tune Fire, California, Sept. 2017](https://www.planet.com/gallery/la-tuna-fire-20170905/) No flames but huge!

### About Sentinel2

* [Bands](https://www.gdal.org/frmt_sentinel2.html): resolution, frequencies, purpose, definitions of "levels" (Level-1B, Level-1C, Level-2A), granules, ortho-rectified tiles, ...
* [Processing in QGIS](https://www.youtube.com/watch?v=9VXv3hYYX3c) by Batbandi Uranchimeg.
* [Centre d'Etude Spatial de la BIOsphere (CESBIO): How it works?](http://www.cesbio.ups-tlse.fr/multitemp/?page_id=1336): French/English explanations/definitons (e.g. [levels](http://www.cesbio.ups-tlse.fr/multitemp/?p=3202), [Cloud shadow detection](http://www.cesbio.ups-tlse.fr/multitemp/?p=911), [python tips](http://www.cesbio.ups-tlse.fr/multitemp/?tag=python), [sentinel2+OpenStreetMap](http://www.cesbio.ups-tlse.fr/multitemp/?p=14818), ...)

### References

* **Satellite data allows real-time detection of potential fires** ([article, Aug. 2018](https://earth.esa.int/web/guest/content/-/article/satellite-data-allows-real-time-detection-of-potential-fires)): seems that using Landsat only. Using Sentinel 2 should give better results ;)
* NASA covers wildfires from many sources ([Phys.org, Jan. 2018](https://phys.org/news/2018-01-nasa-wildfires-sources.html))
* 3 Active Fire Maps: How to Track Real-Time Wildfires Around the World ([gisgeography.com, 2018](https://gisgeography.com/active-fire-maps-real-time-wildfires/))
* **Python from Space Analyzing Open Satellite Imagery Using the Python Ecosystem** ([PyCon 2017, Katherine Scott](https://www.youtube.com/watch?v=rUUgLsspTZA))
    * [github.com/kscottz/PythonFromSpace](https://github.com/kscottz/PythonFromSpace)
* The potentials of Sentinel-2 and LandSat-8 data in green infrastructure extraction, using object based image analysis (OBIA) method ([article, June 2017](https://www.tandfonline.com/doi/full/10.1080/22797254.2017.1419441))
* [Satellite Imagery Analysis with Python](https://medium.com/analytics-vidhya/satellite-imagery-analysis-with-python-3f8ccf8a7c32)
* [Working with Satellite Data, a Gentle Introduction to GDAL Part](https://medium.com/planet-stories/a-gentle-introduction-to-gdal-part-4-working-with-satellite-data-d3835b5e2971)
* ESA global observations of fires for their active climate change initiative: ["Essential climate variables"](https://www.youtube.com/watch?v=XxZjbCEm_nE&list=PLbyvawxScNbtxoBLSxzGDhpaB10J7DSzb&index=13), [data visualisation](http://cci.esa.int/content/tablet-app), specifically their [page on Fire CCI](https://www.esa-fire-cci.org/) (Climate Change Initiative)
    * Mentionning a project named [FireCCISFD11 ](https://www.esa-fire-cci.org/node/280) (burned area dataset) using Sentinel sensors for land monitoring.

## Tools

### Visualize satellite images online

Geographic information system (GIS) platform for distribution of satellite data:

* [US EarthExplorer](https://earthexplorer.usgs.gov/)
* [Sentinel 2 Playground](https://www.sentinel-hub.com/explore/sentinel-playground)
    * [Sentinel Hub pricing](https://www.sentinel-hub.com/pricing-plans)
* [Live view of Landsat imagery](http://live.farearth.com/)
    * [Live position of Landsat satellites](http://live.farearth.com/observer/)

### Image processing tools

* [pySAL](https://pysal.readthedocs.io/en/latest/): Python Spatial Analysis Library
* [Rastervision](https://docs.rastervision.io/en/0.8/): open source framework for Python developers building computer vision models on satellite.
* [Google Cloud Podcast](https://www.gcppodcast.com/post/episode-41-descartes-labs-with-tim-kelton/) discussing the process of (PetaBytes of) satellite imagery almost for free on GCP (using pre-emptible VMs).


### Archves of satellites images

* [LandSat data on Google Cloud Storage](https://cloud.google.com/storage/docs/public-datasets/landsat)
* [Sentinel 2 data on Cloud Storage](https://cloud.google.com/storage/docs/public-datasets/sentinel-2)
* [Google Earth Engine](https://developers.google.com/earth-engine/datasets/): Datasets & JavaScript/[Python API](https://github.com/google/earthengine-api/tree/master/python/examples/ipynb) ([Installaton](https://developers.google.com/earth-engine/python_install)).


### Platforms/APIs for downloading satellite data

* [Awesome Sentinel](https://github.com/Fernerkundung/awesome-sentinel): a curated list of awesome tools, tutorials and APIs for Copernicus Sentinel satellite data.

* [Copernicus Open Access Hub](https://scihub.copernicus.eu/):The Copernicus Open Access Hub (previously known as Sentinels Scientific Data Hub, or SciHub) provides complete, free and open access to Sentinel-1, Sentinel-2, Sentinel-3 and Sentinel-5P user products.
    * [Manual download within the browser](https://www.youtube.com/watch?v=e9F7rQ559ks) in the browser, [stacking bands in QGIS](https://www.youtube.com/watch?v=Hh3bEGiZZ2I)
    * [Sentinelsat](https://sentinelsat.readthedocs.io/en/stable/): a Python package that "makes searching, downloading and retrieving the metadata of Sentinel satellite images from the Copernicus Open Access Hub easy."
    
* [sentinel-hub](https://github.com/sentinel-hub): **Non-free** platform.
    * [EO-Browser](https://apps.sentinel-hub.com/eo-browser/):  a search tool for Sentinel-1, -2, -3, Landsat 5, 7, 8, Modis and Envisat satellite imagery
    * [sentinelhub-py](https://github.com/sentinel-hub/sentinelhub-py): Download and process satellite imagery in Python.
    * [EO-learn](https://medium.com/sentinel-hub/introducing-eo-learn-ab37f2869f5c): "a set of tools to make prototyping of complex EO workflows as easy, fast, and accessible as possible." ([github](https://github.com/sentinel-hub/eo-learn), [docs](https://eo-learn.readthedocs.io/en/latest/))
        * [Land cover classification](https://medium.com/sentinel-hub/land-cover-classification-with-eo-learn-part-1-2471e8098195?source=placement_card_footer_grid---------0-41)
        * [Conflicts & Wildfires](https://medium.com/sentinel-hub/environmental-monitoring-of-conflicts-using-sentinel-2-61f07d76e27b)
* [planet.com's Explorer](https://www.planet.com/explorer): "See the Earth change by navigating through space and time. Identify an area of interest using the search box, draw tools, or supported area definition files",  **Non-free** platform.
* [LandSat python library](https://github.com/developmentseed/landsat-util)


## Installation

```shell
conda create --name sat_3.6 --file environment.yml
```

it contains:

* pySAL (https://pysal.readthedocs.io/en/v1.9/users/installation.html): Python Spatial Analysis Library
* planet (https://pypi.org/project/planet/): Python client library and CLI for [Planet.com](Planet.com)’s public API.
* Rasterio (https://github.com/mapbox/rasterio): reads and writes geospatial raster data.
* geojson (https://github.com/jazzband/python-geojson): Python bindings and utilities for GeoJSON


## Thanks

- Thanks to **Trygve Halsne** from the Norwegian space center who shared this [demo](https://gist.github.com/hevgyrt/f141c985cc9d19aaaa0a4832ed80581a) monitoring vegetation change over a predefined area of interest by means of Sentinel-2 that got us started.
