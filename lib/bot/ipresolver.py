# Website Lookup First https://iplocation.com/
import time
from selenium import webdriver  # for webdriver
import os
import cv2
import numpy

def resolver(ipAddress=""):

    # Country Flags
    countryFlags = os.listdir("flags/")
    #print(countryFlags)

    # Change to Your Chrome Driver Path
    chromeDriverPath = "C:\Program Files\chromedriver\chromedriver.exe"

    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    browser = webdriver.Chrome(chromeDriverPath, options=option)

    # Getting to https://iplocation.com/
    url = f"https://whatismyipaddress.com/ip/{ipAddress}"
    browser.get(url)
    time.sleep(2)

    # Country Result
    countryLoc = browser.find_element_by_xpath("//*[@id='section_left_3rd']/table/tbody/tr[2]/td")
    theCountry = countryLoc.text
    #print(theCountry)

    for i in countryFlags:
        if theCountry.lower() in i:
            return i


def resolverCountryName(ipAddress=""):

    # Country Flags

    # Change to Your Chrome Driver Path
    chromeDriverPath = "C:\Program Files\chromedriver\chromedriver.exe"

    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    browser = webdriver.Chrome(chromeDriverPath, options=option)  #

    # Getting to https://iplocation.com/
    url = f"https://whatismyipaddress.com/ip/{ipAddress}"
    browser.get(url)
    time.sleep(2)

    # Country Result
    countryLoc = browser.find_element_by_xpath("//*[@id='section_left_3rd']/table/tbody/tr[2]/td")
    theCountry = countryLoc.text
    return theCountry