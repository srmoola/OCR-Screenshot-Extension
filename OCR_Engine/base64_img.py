import base64
import cv2
import numpy as np


def base64_to_img(image_link):
    split_base64 = image_link.partition(",")
    im_bytes = base64.b64decode(split_base64[2])

    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
    img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    return img
