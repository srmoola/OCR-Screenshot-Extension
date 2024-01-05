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
norm_img = np.zeros((img.shape[0], img.shape[1]))
img = cv.normalize(img, norm_img, 0, 255, cv.NORM_MINMAX)
f.close()

denoised_image = cv.fastNlMeansDenoising(img_RGB_to_grayscale, None, 50.0, 7, 21)
sharpened = cv.filter2D(denoised_image, -1, kernel_sharpening)
edges_detected = cv.filter2D(sharpened, -1, kernel_edge_detection)
canny_edges = cv.Canny(sharpened, 30, 200)
lap_edges = cv.Laplacian(sharpened, ddepth=-1)

# Gaussian Blur
gauss_blur = cv.GaussianBlur(img_RGB_to_grayscale, ksize=(31, 31), sigmaX=1, sigmaY=1)
# Edge Detection
edges = cv.Laplacian(img_RGB_to_grayscale, ddepth=-1)

threshhold = cv.threshold(gauss_blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

fig, axs = plt.subplots(2, 2, figsize=(15, 8))
axs[0, 0].imshow(img)
axs[0, 0].set_title("Original")
axs[0, 1].imshow(denoised_image, cmap="gray")
axs[0, 1].set_title("Denoising")
axs[1, 0].imshow(sharpened, cmap="gray")
axs[1, 0].set_title("Sharpened")
axs[1, 1].imshow(lap_edges, cmap="gray")
axs[1, 1].set_title("Edge Detection")
plt.show()

w = open("imageprocessing_steps.txt", "w")
all_steps = {
    "Original": img,
    "Denoising": denoised_image,
    "Sharpening": sharpened,
    "Edge Detection 1": edges_detected,
    "Edge Detection 2": lap_edges,
}

step_count = 1

for step, image in all_steps.items():
    get_text = pytesseract.image_to_string(image)
    w.write(f"{step} *******************\n\n")
    w.write(get_text)
    w.write(f"\n\n\n\n")
    step_count += 1
