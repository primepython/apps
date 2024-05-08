import os
import pytesseract
import cv2

def image_processing():
    img = cv2.imread(filename)
    scaled_image = cv2.resize(img, None, fx=7.0, fy=7.0, interpolation=cv2.INTER_LANCZOS4)
    gray = cv2.cvtColor(scaled_image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='eng')
    print(text)

directory = './'
desired_extension = '.jpg'
for filename in os.listdir(directory):
    if os.path.isfile(filename):
        if os.path.splitext(filename)[1] == desired_extension:
            image_processing()
