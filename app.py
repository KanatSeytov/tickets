from configparser import Interpolation
from importlib.resources import path
from PIL import Image
from pytesseract import pytesseract
import re
import os
from pdf2image import convert_from_path
import cv2

absolute_path_to_tickets = 'C:\\Users\\Kanat\\projects\\ml\\tickets\\images\\'
path_to_poppler = 'C:\\Users\\Kanat\\Downloads\\poppler-0.68.0\\bin'
relative_path_to_tickets = 'images\\'
tickets = os.listdir(absolute_path_to_tickets)
path_to_tesseract = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

pytesseract.tesseract_cmd = path_to_tesseract

print(pytesseract.tesseract_cmd)
print('---------------------')
def pdf_to_jpg(tickets):
    jpg_tickets = []
    i = 1
    for ticket in tickets:
        path_to_pdf = relative_path_to_tickets+ ticket
        pages = convert_from_path(path_to_pdf, 350, poppler_path= path_to_poppler)
        
        print(ticket)
        for page in pages:
            
            image_name = "Page_" + str(i) + ".jpg"  
            page.save(image_name, "JPEG")
            jpg_tickets.append(image_name)
            i = i+1    
    return jpg_tickets

jpg_tickets = pdf_to_jpg(tickets)



for image in jpg_tickets:
    print(image)
    img_sized = cv2.imread(image)
    img = img_sized
    # scale_percent = .3 # percent of original size
    # width = int(img_sized.shape[1] * scale_percent)
    # height = int(img_sized.shape[0] * scale_percent)
    # dim = (width, height)
    # img = cv2.resize(img_sized, dim, interpolation = cv2.INTER_AREA)
    # t = pytesseract.image_to_string(Image.open(image))
    # m = re.findall("Passenger", t)
    # if m:
    #     print(m)

    # img = cv2.rectangle(img, (850,750), (1600, 900), (255,0,0), 1)
    tag = img[750:900, 850:1600]
    # img[0:150,0:750] = tag
    gray_image = cv2.cvtColor(tag, cv2.COLOR_BGR2GRAY)
    surname, name = pytesseract.image_to_data(gray_image).splitlines()[-1].split('\t')[-1].split('/')
    print(name, surname)
    # threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # cv2.imshow('threshold image', threshold_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# jpg_tickets = []
# i = 1
# for ticket in tickets:
#     path_to_pdf = relative_path_to_tickets+ ticket
#     pages = convert_from_path(path_to_pdf, 350, poppler_path= path_to_poppler)
    
#     print(ticket)
#     for page in pages:
        
#         image_name = "Page_" + str(i) + ".jpg"  
#         page.save(image_name, "JPEG")
#         jpg_tickets.append(image_name)
#         i = i+1    


# for image in jpg_tickets:
#     print(image)
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#     cv2.imshow('threshold image', threshold_img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


