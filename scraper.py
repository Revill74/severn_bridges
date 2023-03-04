#This module will scrape the Severn Bridge website for the status of each bridge.

import requests
from bs4 import BeautifulSoup

WEB_PATH = "https://nationalhighways.co.uk/travel-updates/the-severn-bridges/"

def bridge_status(path: str) -> list:
    """Parses the web path provided and returns the status of each bridge
     as a list of strings"""
    try:
        # Get web page
        source = requests.get(path).text

        if source:
        # Parse web page through bs4
            soup = BeautifulSoup(source, features="html.parser")
        # Find all instances of bridge status divs
            bridge_status = soup.find_all("div", {"class": "severn-crossing-status__heading"})
        # Assign bridge status to variables
            return [i.text for i in bridge_status]
    except:
        print('sorry, could not find the status')

status = bridge_status(WEB_PATH)
print(f'\n{status[0]}\n{status[1]}')
