import cv2
img12 = cv2.imread("T10TFK_20181116T185639_B12.png")
img11 = cv2.imread("T10TFK_20181116T185639_B11.png")
img04 = cv2.imread("T10TFK_20181116T185639_B04.png")
b12,g12,r12 = cv2.split(img12)
b11,g11,r11 = cv2.split(img11)
b04,g04,r04 = cv2.split(img04)
img = cv2.merge((r12,g11,b04[::2, ::2]))
img = cv2.merge((b12,g12,r12))
# whos
img = cv2.merge((b11,g11,r12))
import matplotlib.pyplot as plt
plt.imshow(img); plt.show()
import numpy as np
np.max(b12)
plt.imshow(img / 256); plt.show()
plt.imshow?
img
np.min(img)
np.max(img)
np.histogram(img)
plt.imshow(img12); plt.show()
plt.imshow(img12 * 3); plt.show()
plt.imshow(img12 * 5); plt.show()
plt.imshow(img * 5); plt.show()
plt.imshow(img12 - img11); plt.show()
img_a = img.copy()
img_a[img_a > 20] = 20
plt.imshow(img_a); plt.show()
plt.imshow(img_a) * 14; plt.show()
plt.imshow(img_a * 14); plt.show()
img = cv2.merge((b12,g11,r11))
plt.imshow(img * 5); plt.show()


####

import cv2
img12 = cv2.imread("T10TFK_20181116T185639_B12.png")
img11 = cv2.imread("T10TFK_20181116T185639_B11.png")
img04 = cv2.imread("T10TFK_20181116T185639_B04.png")
b12,g12,r12 = cv2.split(img12)
b11,g11,r11 = cv2.split(img11)
b04,g04,r04 = cv2.split(img04)
img = cv2.merge((r12,g11,b04[::2, ::2]))
import matplotlib.pyplot as plt
plt.imshow(img * 5); plt.show()
img
cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
plt.imshow(img_hsv); plt.show()
h, s, v = cv2.split(img_hsv)
h
plt.imshow(h); plt.show()
