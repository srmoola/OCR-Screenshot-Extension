import cv2 as cv
from base64_img import base64_to_img
import pytesseract
import numpy as np
import matplotlib.pyplot as plt

# kernels for opencv filters
kernel_sharpening = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
kernel_edge_detection = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

f = open("image.txt", "r")
img = base64_to_img(f.read())
img_RGB_to_grayscale = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
f.close()

denoised_image = cv.fastNlMeansDenoising(img_RGB_to_grayscale, None, 50.0, 7, 21)
sharpened = cv.filter2D(denoised_image, -1, kernel_sharpening)
edges_detected = cv.filter2D(sharpened, -1, kernel_edge_detection)
edged = cv.Canny(sharpened, 30, 200)

fig, axs = plt.subplots(2, 2, figsize=(15, 8))
axs[0, 0].imshow(img)
axs[0, 0].set_title("Original")
axs[0, 1].imshow(denoised_image, cmap="gray")
axs[0, 1].set_title("Denoising")
axs[1, 0].imshow(sharpened, cmap="gray")
axs[1, 0].set_title("Sharpened")
axs[1, 1].imshow(edges_detected, cmap="gray")
axs[1, 1].set_title("Edge Detection")
plt.show()

w = open("imageprocessing_steps.txt", "w")
all_steps = {
    "Original": img,
    "Denoising": denoised_image,
    "Sharpening": sharpened,
    "Edge Detection 1": edges_detected,
    "Edge Detection 2": edged,
}

step_count = 1

for step, image in all_steps.items():
    get_text = pytesseract.image_to_string(image)
    w.write(f"{step} *******************\n\n")
    w.write(get_text)
    w.write(f"\n\n\n\n")
    step_count += 1
