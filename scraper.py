#This module will scrape the Severn Bridge website for the status of each bridge.

import requests
from bs4 import BeautifulSoup
from datetime import datetime


class BridgeStatus:
    """Class for keeping bridge status data together"""
    def __init__(self):
        self.m4 = self.bridge_status()[0]
        self.m48 = self.bridge_status()[1]
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def bridge_status(self) -> tuple:
        """Parses the web path provided and returns the status of each bridge
        as a tuple of strings"""

        WEB_PATH = "https://nationalhighways.co.uk/travel-updates/the-severn-bridges/"
        try:
            # Get web page
            source = requests.get(WEB_PATH).text

            if source:
                soup = BeautifulSoup(source, features="html.parser")
                bridge_status = soup.find_all("div", {"class": "severn-crossing-status__heading"})

                m4 = bridge_status[0].text
                m48 = bridge_status[1].text

                return (m4, m48)
        except:
            print('sorry, could not find the status')

bridges = BridgeStatus()
bridges_dict = vars(bridges)    # Creates dict of bridges attributes




