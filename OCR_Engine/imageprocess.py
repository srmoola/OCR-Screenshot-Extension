import cv2 as cv
from base64_img import base64_to_img
import pytesseract

f = open("image.txt", "r")
img = base64_to_img(f.read())
img_RGB_to_grayscale = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
get_text = pytesseract.image_to_string(img)
denoised_image = cv.fastNlMeansDenoising(img_RGB_to_grayscale)
get_text2 = pytesseract.image_to_string(denoised_image)

print("First Image Text: ")
print(get_text)
print("\n\n\n\n\n")
print("Second Image Text: ")
print(get_text2)

cv.imshow("Image", denoised_image)
cv.waitKey(0)
cv.destroyAllWindows()
