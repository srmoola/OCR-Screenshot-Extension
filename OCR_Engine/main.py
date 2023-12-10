import pandas as pd
import cv2
import pytesseract

from matplotlib import pyplot as plt

from base64_img import base64_to_img

img = base64_to_img()

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
