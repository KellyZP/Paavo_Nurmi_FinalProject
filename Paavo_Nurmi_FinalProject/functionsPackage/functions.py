# Group Name: Paavo Nurmi (Gavin Reinhard, Sarah Ouellette, Zach Kelly, & Jakob Fisher)
# Email: ,,ouellesj@mail.uc.edu,fishe2jo@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: Function module that provides the functions to decrypt the location data and display our team photo.
# Citations: https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
# Anything else that's relevant: 
# functions.py

import json
from PIL import Image

def decrypt_message(team_name,dict_path,encrypted_path):
    with open(encrypted_path, 'r') as f:
        temp = f.read()
    data = json.loads(temp)
    message = data[team_name]
    
    english = []
    with open(dict_path) as file:
        while line := file.readline():
            english.append(line.rstrip())
            
    location = ''
    for item in message:
        location += english[int(item) - 1] + ' '
    return location

def display_picture():
    #Open image using Image module
    im = Image.open("Picture.JPEG").rotate(-90) # THIS IS AN EXAMPLE ---- CHANGE TO ACUTAL PICTURE
    #Show actual Image
    im.show()
