from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("C:/Users/user/Downloads/chromedriver_win32")
browser.get(START_URL)
time.sleep((10))
def scrap():
    headers=["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planet_data=[] 

    soup=BeautifulSoup(browser.page_source,"html.parser")
    for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
        li_tags=ul_tag.find_all("li")
        temp_list=[]
        for index,li_tag in enumerate(li_tag)