# -*- coding: utf-8 -*-

"""
A Flask app to trigger some image processing.
"""

from PIL import Image, ImageFilter
from datetime import datetime
import numpy as np
class MonitoredRegion():
    """
    Manage various set of satellite images
    """
    def __init__(self, path_to_channels):
        self.path_to_channels = path_to_channels
        self.image = SatelliteImage(path_to_channels)


class SatelliteImage():
    """
    Store and process information about a single satellite image.
    - coordinates of boundaries
    - Sentinel 2 metadata
    - fires detected on it, or not
    - store the image if relevant, remove it otherwise
    """
    def __init__(self, path_to_channels: str):
        self.sentinel_metadata = {} # coordinates, resolution, cloud coverage, ...
        self.channels = {} # raw and RGB for each channel
        # {"path_to_file": x for x in path_to_channels.glob("*.png") if x.is_file()}

    def get_channels(self):
        """
        Get information about the various channels from Sentinel's zip/folder
        """
        pass


    def locate_fire_from_image(self):
        """
        Returns coordinates of fires detected in the satellite image.
        """
        return "well... coming soon ;)"


    def convert_jp2_to_png(self):
        """
        Convert from JPEG2000 to PNG format
        https://github.com/DataForGood-Norway/FireFromSpace/blob/master/copernicus/convert_jp2_to_png.sh
        """
        pass


    def split_channels_into_RGBs(self, channels_images):
        """
        use OpenCV to split every channel into RGB
        (https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_basic_ops/py_basic_ops.html#splitting-and-merging-image-channels),
        """
        pass


    def combine_RGB_into_image(self, R_channel, G_channel, B_channel) -> Image:
        """
        merge this channel back together to mimic the False Color (Urban) filter of Sentinel Playground
        (https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=39.80220607474974&lng=-121.51874542236328&zoom=11&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2018-05-01%7C2018-11-16&atmFilter=&showDates=false)
        """
        pass


    def get_HSV_from_image(self):
        """
        converted this new image to HSV to extract its hue
        """