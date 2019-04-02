# -*- coding: utf-8 -*-

"""
Image processing.

Image manipulation:
- https://docs.python-guide.org/scenarios/imaging/#example
- https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html
"""

# What image processing library is best?
import cv2
import dill
import numpy as np
from PIL import Image, ImageFilter, ImageOps
from typing import List, Set, Dict, Tuple, Optional
# from scipy.ndimage import imread
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

def split_image_into_RGB(path_to_image: str) -> Tuple[int]:
    """
    use OpenCV to split every channel into RGB
    (https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_basic_ops/py_basic_ops.html#splitting-and-merging-image-channels),
    """
    print(f"Splitting '{path_to_image}' into RGB...")
    img = cv2.imread(path_to_image)
    (b, g, r) = cv2.split(img)
    return (r, g, b)


def normalize2(pil_img):
    return ImageOps.autocontrast(pil_img)


def normalize(img):
    '''
    Normalize the exposure of an image.
    @args:
    {numpy.ndarray} img: an array of image pixels with shape:
        (height, width)
    @returns:
    {numpy.ndarray} an image with shape of `img` wherein
        all values are normalized such that the min=0 and max=255
    '''
    _min = img.min()
    _max = img.max()
    return (img - _min) * 255 / (_max - _min)


def convert_jp2_to_png(jp2):
    """
    Convert from JPEG2000 to PNG format
    https://en.wikipedia.org/wiki/JPEG_2000
    https://en.wikipedia.org/wiki/Extensible_Metadata_Platform
    https://github.com/DataForGood-Norway/FireFromSpace/blob/master/copernicus/convert_jp2_to_png.sh
    https://stackoverflow.com/questions/44051852/how-to-read-jpg2000-with-python
    JPEG2000 for Python: https://softwarerecs.stackexchange.com/questions/51486/jpeg2000-for-python
    - https://pillow.readthedocs.io/en/4.1.x/handbook/image-file-formats.html#jpeg-2000
    - https://glymur.readthedocs.io/en/latest/introduction.html
    """
    pass


def combine_RGB_into_image(r_channel, g_channel, b_channel):
    """
    merge this channel back together to mimic the False Color (Urban) filter of Sentinel Playground or other best suited filter.
    (https://apps.sentinel-hub.com/sentinel-playground/?source=S2&lat=39.80220607474974&lng=-121.51874542236328&zoom=11&preset=3_FALSE_COLOR__URBAN_&layers=B01,B02,B03&maxcc=20&gain=1.0&gamma=1.0&time=2018-05-01%7C2018-11-16&atmFilter=&showDates=false)
    """
    return cv2.merge((b_channel, g_channel, r_channel))


def get_HSV_from_image(img: np.ndarray) -> np.ndarray:
    """
    converted this new image to HSV space to extract its hue
    """
    return  cv2.cvtColor(img, cv2.COLOR_RGB2HSV) 


def apply_color_mask(hsv_img):
    lower_bound = np.array([0,50,50]) 
    upper_bound = np.array([20,255,255]) 
    mask = cv2.inRange(hsv_img, lower_bound, upper_bound) | cv2.inRange(hsv_img, np.array([160, 50, 50]), np.array([180, 255, 255])) 
    return cv2.bitwise_and(hsv_img, hsv_img, mask=mask)


def plot_HSV(rgb_img: np.ndarray):
    pixel_colors = rgb_img.reshape((np.shape(rgb_img)[0]*np.shape(rgb_img)[1], 3))
    norm = colors.Normalize(vmin=-1.,vmax=1.)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()


    h, s, v = cv2.split(get_HSV_from_image(rgb_img))
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")
    axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
    axis.set_xlabel("Hue")
    axis.set_ylabel("Saturation")
    axis.set_zlabel("Value")
    plt.show()

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")

	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)
