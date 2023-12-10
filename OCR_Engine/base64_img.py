import base64
import cv2
import numpy as np


def base64_to_img() -> any:
    with open("image.txt", "r") as f:
        im_bytes = base64.b64decode(f.read())

    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
    img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    return img
