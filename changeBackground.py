from bs4 import BeautifulSoup
import os
import urllib.request
import requests
import ctypes

# Check if there is currently an image saved, and delete it if it does exist
if os.path.exists(r"C:\Users\uther\OneDrive\Documents\backgroundAPOD\APOD.jpg"):
    os.remove(r"C:\Users\uther\OneDrive\Documents\backgroundAPOD\APOD.jpg")

# Scrape img from page and store the URL to it's source, if there is one
page = requests.get("https://apod.nasa.gov/apod/astropix.html")
soup = BeautifulSoup(page.text, "html.parser")
APOD = soup.find_all('img')
# Get the image's description/explanation
description = soup.find_all('p')

# Print the image's description to the cmd shell
if len(description) != 0 :
        print(description[0])

# If there is an image today, set it as the background. 
if len(APOD) != 0:
    APODURL = "https://apod.nasa.gov/apod/" + str(APOD[0]["src"])
    # Store the Image locally
    image = open(r"C:\Users\uther\OneDrive\Documents\backgroundAPOD\APOD.jpg", "wb")
    image.write(urllib.request.urlopen(APODURL).read())
    # Set Image as background
    ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\uther\OneDrive\Documents\backgroundAPOD\APOD.jpg", 0)

# Otherwise, use the default
else:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\uther\OneDrive\Documents\backgroundAPOD\default.jpg", 0)

