import cv2 as cv
from base64_img import base64_to_img
import numpy as np
import matplotlib.pyplot as plt

f = open("image.txt", "r")
img = base64_to_img(f.read())
f.close()

# Normalization
norm_img = np.zeros((img.shape[0], img.shape[1]))
img = cv.normalize(img, norm_img, 0, 255, cv.NORM_MINMAX)

# Gray Scaling
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

# Denoising
img = cv.fastNlMeansDenoising(img, None, 10.0, 7, 21)

# Sharpening
kernel_sharpening = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
img = cv.filter2D(img, -1, kernel_sharpening)

# Thresholding / Binarization
img = cv.threshold(
    img, 0, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C + cv.ADAPTIVE_THRESH_MEAN_C
)[1]

cv.imshow("Finished", img)
cv.waitKey(0)
cv.destroyAllWindows()
