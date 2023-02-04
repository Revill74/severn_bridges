#This module will scrape the Severn Bridge website for the status of each bridge.

import requests
from bs4 import BeautifulSoup

WEB_PATH = "https://nationalhighways.co.uk/travel-updates/the-severn-bridges/"

#Get web page
source = requests.get(WEB_PATH).text

#Parse web page through bs4
soup = BeautifulSoup(source, features="html.parser")

#Find all instances of bridge status divs
bridge_status = soup.find_all("div", {"class": "severn-crossing-status__heading"})

#Assign bridge status to variables
m4 = bridge_status[0].text
m48 = bridge_status[1].text