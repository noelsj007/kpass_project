import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import re
def aadhaarScrapper(image):

    # img = cv2.imread("/home/noelsj/Documents/aahaarmy.jpeg")
    img = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    plt.imshow(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
    text1 = pytesseract.image_to_data(threshed,output_type='data.frame')
    text2 = pytesseract.image_to_string(threshed, lang="ind")
    print(text2)
    text = text1[text1.conf != -1]
    regex = r'\d{4}\s\d{4}\s\d{4}'
    regex1 = r'DOB\s*:\s*(\d{1,2}/\d{1,2}/\d{4})'
    aadhaar_no = re.findall(regex, text2)
    dob = re.findall(regex1, text2)

    print(aadhaar_no, dob)
    num_list = aadhaar_no
    num_str = num_list[0]  # Extract the string from the list
    num_str_without_spaces = num_str.replace(' ', '')  # Remove the spaces from the string
    num_int = int(num_str_without_spaces)  # Convert the string to an integer
    print(num_int)
    lines = text.groupby('block_num')['text'].apply(list)
    conf = text.groupby(['block_num'])['conf'].mean()

    return num_int
    
