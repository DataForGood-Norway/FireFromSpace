# -*- coding: utf-8 -*-

"""
A Flask app to trigger some image processing from a webapp.
"""

from datetime import datetime

class ImageProcess():
    """
    Process a single satellite image to locate fires on it.
    """
    def __init__(path_to_images):
        self.path_to_images = path_to_images


    def locate_fire_from_image(path_to_images):
        """
        Returns coordinates of fires detected in the satellite image.
        """
        pass


    def convert_jp2_to_png():
        """
        Convert from JPEG2000 to PNG format
        https://github.com/DataForGood-Norway/FireFromSpace/blob/master/copernicus/convert_jp2_to_png.sh
        """
        pass


    def get_RGB_from_channels(channels_images):
        """
        use OpenCV to split every channel into RGB
        (https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_basic_ops/py_basic_ops.html#splitting-and-merging-image-channels),
        """
        pass


    def combine_channels_into_RGB_image(channels_RGB):
        """
        merge this channel back together to mimic the False Color (Urban) filter of Sentinel Playground
        (https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=39.80220607474974&lng=-121.51874542236328&zoom=11&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2018-05-01%7C2018-11-16&atmFilter=&showDates=false)
        """
        pass


    def get_HSV_from_image(image):
        """
        converted this new image to HSV to extract its hue
        """

)