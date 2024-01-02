from base64_img import base64_to_img
import pytesseract

img = base64_to_img()
text = pytesseract.image_to_string(img)
print(text)
