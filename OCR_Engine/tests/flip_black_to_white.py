from is_black_or_white import is_black_or_white
from base64_img import base64_to_img
import cv2 as cv
import numpy as np
import pytesseract


f = open("image.txt", "r")
img = base64_to_img(f.read())
f.close()

h = img.shape[0]
w = img.shape[1]

new_image = np.ones((h, w)) * 255


for i in range(h):
    for j in range(w):
        if (img[i, j] != 0).all():
            new_image[i, j] = 0

cv.imshow("Image", new_image)
cv.waitKey(0)
cv.destroyAllWindows()

print(pytesseract.image_to_string(new_image))
