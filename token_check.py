#For image sample, please refer to token_check_sample.png
import pytesseract
import cv2

#Recognition function
def image_processing():
    img = cv2.imread("./{image}")
    scaled_image = cv2.resize(img, None, fx=3.0, fy=3.0)
    gray = cv2.cvtColor(scaled_image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='eng')
    text = text.replace('\n', ' ').strip()

#Time marker positioning
    time_marker= '@'
    time_marker_index = text.find(time_marker)
    if text[-2].isdigit():
        minutes= text[(time_marker_index+1):(time_marker_index+4)]
        seconds = text[-3:]
        time = [minutes, seconds]
    else:
        time = 'FULL'
#Delimeter posiitoning
    delimeter = '/'
    delimeter_index = text.find(delimeter)
    if text[(delimeter_index-2)].isdigit():
        keys_tokens = text[(delimeter_index-2):(delimeter_index+3)]
    else:
        keys_tokens = text[(delimeter_index-1):(delimeter_index+3)]

    if text[(delimeter_index-2)].isdigit():
        get_title = text[:(delimeter_index-2)]
    else:
        get_title = text[:(delimeter_index-1)]
# Print the extracted text
    keys_tokens_info ={'title':get_title, 'amount':keys_tokens, 'next_auto_refill':time}
    print(keys_tokens_info)
  
image_processing()
