# Group Name: Paavo Nurmi (Gavin Reinhard, Sarah Ouellette, Zach Kelly, & Jakob Fisher)
# Email: ,,,fishe2jo@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: Main module that invokes the functions from the function package.
# Citations:
# Anything else that's relevant: 
# main.py

from functionsPackage.functions import *

decryptedData = decrypt_message('Paavo Nurmi','english.txt','EncryptedGroupHints Spring 2023 Section 001.json')
print(decryptedData)

display_picture()
# the image will display through an app on your OS, you may get a prompt to choose preferred app