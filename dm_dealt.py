import os
import pytesseract
import cv2


def damage_recognition():
    directory = './'
    desired_extension = '.png'
    for filename in os.listdir(directory):
        if os.path.isfile(filename):
            if os.path.splitext(filename)[1] == desired_extension:
                def img_proc():
                    img = cv2.imread(filename)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    scaled_image = cv2.resize(gray, None, fx=7.0, fy=7.0)
                    thresh = cv2.threshold(scaled_image, 175, 255, cv2.THRESH_BINARY_INV)[1]
                    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
                    opening = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
                    text = pytesseract.image_to_string(opening, lang='eng')
                    m_find = text.find("M")
                    damage_dealt = text[:m_find]
                    damage_dealt = damage_dealt.replace(",", ".")
                    def dm_dealt():
                        print(float(damage_dealt))
                    dm_dealt()
                img_proc()
damage_recognition()
