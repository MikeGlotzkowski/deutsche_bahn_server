from . import db_url
from . import resources
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

class Db_service(object):
    def get():
        url = db_url.create_from(resources.LOCATION_RO,
                                 resources.LOCATION_MUC_OST)

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")

        result_view = soup.find(id="resultsOverview")
        result_view_rows = result_view.find_all("tbody", ["boxShadow"])

        result_1 = result_view_rows[0].find("tr", ["firstrow"])
        result_2 = result_view_rows[1].find("tr", ["firstrow"])
        result_3 = result_view_rows[2].find("tr", ["firstrow"])

        time_1 = result_1.find("td", ["time"]).decode_contents().split()[0]
        time_2 = result_2.find("td", ["time"]).decode_contents().split()[0]
        time_3 = result_3.find("td", ["time"]).decode_contents().split()[0]
        return [time_1, time_2, time_3]
