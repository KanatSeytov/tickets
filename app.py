from configparser import Interpolation
from importlib.resources import path
from PIL import Image
from pytesseract import pytesseract
import re
import os
from pdf2image import convert_from_path
import cv2
import datetime

absolute_path_to_tickets = 'C:\\Users\\Kanat\\projects\\ml\\new\\tickets\\images\\'
path_to_poppler = 'C:\\Users\\Kanat\\Downloads\\poppler-0.68.0\\bin'
relative_path_to_tickets = 'images\\'
tickets = os.listdir(absolute_path_to_tickets)
path_to_tesseract = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

pytesseract.tesseract_cmd = path_to_tesseract


def pdf_to_jpg(tickets):
    jpg_tickets = []
    i = 1
    for ticket in tickets:
        path_to_pdf = relative_path_to_tickets+ ticket
        pages = convert_from_path(path_to_pdf, 350, poppler_path= path_to_poppler)

        for page in pages:
            
            image_name = "Page_" + str(i) + ".jpg"  
            page.save(image_name, "JPEG")
            jpg_tickets.append(image_name)
            i = i+1    
    return jpg_tickets

jpg_tickets = pdf_to_jpg(tickets)

def transform_image_to_text(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # this line transform data and split it by slash like in tickets of FlyArystan
    text = pytesseract.image_to_data(gray_image).splitlines()[-1].split('\t')[-1].split('/') 
    return text

def get_useraname_from_image(image):
    return image[755:855, 850:1600]

def get_travel_date_from_image(image):
    return image[400:480, 80:450]
    
def openImage(link):
    return cv2.imread(link)

def normilize_image(img_sized):
    width = 2893 #int(img_sized.shape[1] * scale_percent)
    height = 4094  #int(img_sized.shape[0] * scale_percent)
    dim = (width, height)
    image = cv2.resize(img_sized, dim, interpolation = cv2.INTER_AREA)
    return image

def run():
    for file in jpg_tickets:
        img_sized = openImage(file)
        img = normilize_image(img_sized)

        # extract user name and surname in image
        img = cv2.rectangle(img, (850,755), (1600, 855), (255,0,0), 1)
        user_name = get_useraname_from_image(img)

        # extract user travel date of user in image
        img = cv2.rectangle(img, (80,400), (450,480), (0,255,0), 1)
        travel_date =get_travel_date_from_image(img)

        # img[0:150,0:750] = user_name
        # img[0:80,0:370]  = travel_date

        user_name = transform_image_to_text(user_name)
        surname, name = user_name

        travel_date = transform_image_to_text(travel_date)
        day, month, year = travel_date
        date = f"{day}/{month}/{year}"
        datetime.datetime.strptime(date, '%d/%m/%Y')

        cv2.imshow('threshold image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    run()