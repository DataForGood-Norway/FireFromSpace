# -*- coding: utf-8 -*-

"""
Satellite Image processing.

Image manipulation:
- https://docs.python-guide.org/scenarios/imaging/#example
- https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html
"""


import cv2
import dill
from PIL import Image
from datetime import datetime
import numpy as np
from pathlib import Path, PosixPath
from datetime import datetime, timedelta
import image_processing
import matplotlib.pyplot as plt

class MonitoredRegion():
    """
    Manage various set of satellite images
    """

    def __init__(self, region_coordinates):
        self.region_coordinates = None
        self.path_to_Sentinels_products = None
        self.images = []

    def query_scihub_copernicus(self):
        """
        https://scihub.copernicus.eu/
        https://scihub.copernicus.eu/twiki/do/view/SciHubWebPortal/APIHubDescription
        https://scihub.copernicus.eu/userguide/BatchScripting#Query_via_wget
        """
        path_to_Sentinels_products = None
        return path_to_Sentinels_products


class SatelliteImage():
    """
    Store and process information about a single satellite image.
    - coordinates of boundaries
    - convert jp2 to png (https://docs.opencv.org/3.0-beta/modules/imgcodecs/doc/reading_and_writing_images.html)
    - Sentinel 2 metadata
    - fires detected on it, or not
    - store the image if relevant, remove it otherwise
    """

    def __init__(self, path_to_bands: str):
        # coordinates, resolution, cloud coverage, ...
        self.bands = {}
        for pth in path_to_bands.glob("*.png"):
            if pth.is_file():
                (tile_name, dtime, channel) = str(pth.resolve()).split(".")[0].split("_")
                obj = {
                    "path": pth,
                    "tile_name": tile_name,
                    "datetime_str": dtime,
                    "datetime": datetime.strptime(dtime, '%Y%m%dT%H%M%S'),
                    "RGB": None}
                self.bands[channel] = obj
        self.sentinel_metadata = {}
        self.coordinates = None

    def split_bands_into_RGBs(self):
        for ch in self.bands:
            if Path(ch).is_file():
                with open(ch, 'rb') as in_strm:
                    self.bands[ch]["RGB"] = dill.load(in_strm)
            else:
                self.bands[ch]["RGB"] = \
                    image_processing.split_image_into_RGB(str(self.bands[ch]["path"].resolve()))
                with open(ch, "wb") as dill_file:
                    dill.dump(self.bands[ch]["RGB"], dill_file)

    def filter_image(self, filter_name):
        if filter_name == "FALSE_COLOR_URBAN":
            min_common_size = min([self.bands[ch]["RGB"][0].shape[0] for ch in ["B04", "B11", "B12"]])
            r_step = int(self.bands["B12"]["RGB"][0].shape[0] / min_common_size)
            r_intensity = self.bands["B12"]["RGB"][0][::r_step, ::r_step]
            g_step = int(self.bands["B11"]["RGB"][0].shape[0] / min_common_size)
            g_intensity = self.bands["B11"]["RGB"][1][::g_step, ::g_step]
            b_step = int(self.bands["B04"]["RGB"][0].shape[0] / min_common_size)
            b_intensity = self.bands["B04"]["RGB"][2][::b_step, ::b_step]
            # return cv2.merge((b_intensity, g_intensity, r_intensity))
            # return cv2.merge((r_intensity, g_intensity, b_intensity))
            return image_processing.combine_RGB_into_image(r_intensity, g_intensity, b_intensity)
        else:
            raise AttributeError(f"The filter name '{filter_name}' isn't recognized! Consider implementing it!")

    def locate_fire_from_image(self):
        """
        Returns coordinates of fires detected in the satellite image.
        https://realpython.com/python-opencv-color-spaces/#color-spaces-and-reading-images-in-opencv
        http://scikit-image.org/docs/stable/auto_examples/features_detection/plot_blob.html#sphx-glr-auto-examples-features-detection-plot-blob-py
        http://scikit-image.org/docs/stable/auto_examples/color_exposure/plot_ihc_color_separation.html#sphx-glr-auto-examples-color-exposure-plot-ihc-color-separation-py
        http://scikit-image.org/docs/stable/auto_examples/edges/plot_canny.html#sphx-glr-auto-examples-edges-plot-canny-py
        http://scikit-image.org/docs/stable/auto_examples/segmentation/plot_random_walker_segmentation.html#sphx-glr-auto-examples-segmentation-plot-random-walker-segmentation-py
        http://scikit-image.org/docs/stable/auto_examples/color_exposure/plot_adapt_rgb.html#sphx-glr-auto-examples-color-exposure-plot-adapt-rgb-py
        """
        return "well... coming soon ;)"



def main():
    region_coordinates = []
    region = MonitoredRegion(region_coordinates)
    path_to_Sentinels_products = region.query_scihub_copernicus()

    path_to_bands = Path("..") / "data"
    sat_image = SatelliteImage(path_to_bands)
    sat_image.split_bands_into_RGBs()
    img1 = sat_image.filter_image("FALSE_COLOR_URBAN") # showing smoke in red, but too dark if not 'img*5'
    
    # normalize the image using Pillow
    pil_im = Image.fromarray(img1.astype("uint8"), "RGB")
    img2 = image_processing.normalize2(pil_im) # showing smoke in red

    plt.subplot(231),plt.imshow(img1,'gray'),plt.title('FALSE_COLOR_URBAN')
    plt.subplot(232),plt.imshow(img2,'gray'),plt.title('FALSE_COLOR_URBAN normalized PIL')

    src = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    equ1 = cv2.equalizeHist(src)
    # A more general approach would be transforming RGB values into another space that
    # contains a luminescence/intensity value (Luv, Lab, HSV, HSL), apply histeq only in intensity plane and perform the inverse transform.

    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img1],[i],None,[256],[0,256])
        plt.subplot(233),plt.plot(histr,color = col)
        plt.xlim([0,256])

    plt.subplot(234),plt.imshow(equ1,'gray'),plt.title('FALSE_COLOR_URBAN equalized cv2')
    plt.show()

    from IPython import embed; embed()

if __name__ == '__main__':
    main()
