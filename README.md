# FireFromSpace

_Detect fire from satellite images_ 

Be it forest fires or villages being attacked, some fires can be detected from space. We hope to build a tool for monitoring the environment and watching for the safety of defenseless civilians.

## Join The Project

Join us on [Slack](http://dataforgood.no/contact-us/), then join our [channel](https://dataforgood-norway.slack.com/messages/CFJFRAKT2/).


### We Need Your Help

See [all tasks](https://github.com/DataForGood-Norway/FireFromSpace/issues?q=is%3Aopen) organised in:

* [Milestones/Objectives](https://github.com/DataForGood-Norway/FireFromSpace/milestones),
* [Kanban boards](https://github.com/DataForGood-Norway/FireFromSpace/projects) to track their development.

The project is just starting, but come help us or learn with us. Don't hesitate to contact us and ask questions on [our Slack channel](https://dataforgood-norway.slack.com/messages/CFJFRAKT2/).


## What Are We Doing?

While satellite's images are [free to access](https://apps.sentinel-hub.com/sentinel-playground), the amount of images to process in order to watch the whole of earth is just too big (over 4 Terabytes of fresh products published every day on the Copernicus portals).

This tool won't allow us to monitor the entire planet. But it will be an opensource webapp for anyone to use, giving them the possibility to monitor large fires within a part of earth (e.g. a state monitoring a dry forest, garbage burning illegally and toxic for its neighbours, or more importantly the United Nations watching for genocide and human rights atrocities.

This project is mainly split into 2 parts:

- **Processing Satellite's images for fire detection**: to measure and to locate the fire as accurately as possible. This module should be easily usable by any developer with a computer, therefore without worrying about any cost of cloud resources.

- **a webapp**: For the other users who prefer a user interface, a webapp should allow them to rent cloud resources required for monitoring the part of earth they are interested in, or to share the cost with others watching the same area already.


## Goal

Our goals is to help monitor fires all over the globe for plenty of good reasons.


## More Information

+ Thanks to **Trygve Halsne** from the Norwegian space center who shared this [demo](https://gist.github.com/hevgyrt/f141c985cc9d19aaaa0a4832ed80581a) monitoring vegetation change over a predefined area of interest by means of Sentinel-2.


## Spotted fires from space

- [Wildfires in California, USA](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=36.22004146127195&lng=-118.61878395080566&zoom=13&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=30&gain=1.0&gamma=1.0&time=2018-05-01%7C2018-11-08&atmFilter=&showDates=true) (Nov. 8th 2018).
- Spotting Colombia deforestation (before on [2018, Feb. 9th](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=2.161990957069677&lng=-72.38258600234985&zoom=15&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2017-08-01%7C2018-02-09&atmFilter=&showDates=true) and after on [2018, Feb. 10th](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=2.161990957069677&lng=-72.38258600234985&zoom=15&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2017-08-01%7C2018-02-10&atmFilter=&showDates=true), moving on on [2018, Feb 20th](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=2.161990957069677&lng=-72.38258600234985&zoom=15&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2017-08-01%7C2018-02-20&atmFilter=&showDates=true).
- Deonar's garbage burning [(2016, Janv. 30th)](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=19.06994618081784&lng=72.92392015457153&zoom=15&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2015-07-01%7C2016-01-30&atmFilter=&showDates=true),  continuously polluting the air until [2016, March 28th](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=19.06994618081784&lng=72.92392015457153&zoom=15&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2015-09-01%7C2016-03-28&atmFilter=&showDates=true).
- [Southern Portugal, August 2018](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=37.274530905549355&lng=-8.45998764038086&zoom=13&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=39&gain=1.0&gamma=1.0&time=2018-02-01%7C2018-08-08&atmFilter=&showDates=false).
- [Central Portugal, Summer 2017](https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=39.98843197151454&lng=-8.052978515625&zoom=11&preset=2_COLOR_INFRARED__VEGETATION_&layers=B01,B02,B03&maxcc=100&gain=1.0&gamma=1.0&time=2017-01-01%7C2017-07-07&atmFilter=&showDates=false).

## References

* **Satellite data allows real-time detection of potential fires** ([article, Aug. 2018](https://earth.esa.int/web/guest/content/-/article/satellite-data-allows-real-time-detection-of-potential-fires)): seems that using Landsat only. Using Sentinel 2 should give better results ;)
* NASA covers wildfires from many sources ([Phys.org, Jan. 2018](https://phys.org/news/2018-01-nasa-wildfires-sources.html))
* 3 Active Fire Maps: How to Track Real-Time Wildfires Around the World ([gisgeography.com, 2018](https://gisgeography.com/active-fire-maps-real-time-wildfires/))
* **Python from Space Analyzing Open Satellite Imagery Using the Python Ecosystem** ([PyCon 2017, Katherine Scott](https://www.youtube.com/watch?v=rUUgLsspTZA))
    * [github.com/kscottz/PythonFromSpace](https://github.com/kscottz/PythonFromSpace)
* The potentials of Sentinel-2 and LandSat-8 data in green infrastructure extraction, using object based image analysis (OBIA) method ([article, June 2017](https://www.tandfonline.com/doi/full/10.1080/22797254.2017.1419441))


## Tools

* [US EarthExplorer](https://earthexplorer.usgs.gov/)
* [Sentinel 2 Playground](https://www.sentinel-hub.com/explore/sentinel-playground)
    * [Sentinel Hub pricing](https://www.sentinel-hub.com/pricing-plans)
* [Live view of Landsat imagery](http://live.farearth.com/)
    * [Live position of Landsat satellites](http://live.farearth.com/observer/)
* [Google Cloud Podcast](https://www.gcppodcast.com/post/episode-41-descartes-labs-with-tim-kelton/) for processing (PetaBytes) satellite imagery almost for free on GCP (using pre-emptible VMs).

    * [LandSat data on Google Cloud Storage](https://cloud.google.com/storage/docs/public-datasets/landsat)
    * [Sentinel 2 data on Cloud Storage](https://cloud.google.com/storage/docs/public-datasets/sentinel-2)
    * [Google Earth Engine](https://developers.google.com/earth-engine/datasets/): Datasets & JavaScipt/[Python API](https://github.com/google/earthengine-api/tree/master/python/examples/ipynb) ([Installaton](https://developers.google.com/earth-engine/python_install)).