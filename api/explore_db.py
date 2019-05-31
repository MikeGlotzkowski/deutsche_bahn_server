from . import db_url
from . import resources
import requests
import urllib.request
import time
import datetime
from bs4 import BeautifulSoup


class Db_service(object):
    def get():
        date = datetime.datetime.strptime(str(datetime.datetime.now()), "%Y-%m-%d  %H:%M:%S.%f")
        url = db_url.create_from(resources.LOCATION_MUC_OST,
                                 resources.LOCATION_RO,
                                 date.day, date.month, str(date.year)[-2:], date.hour, date.min)
        return Db_service.get_for_url(url)


    
    def get_for_url(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")

        result_view = soup.find(id="resultsOverview")
        result_view_rows = result_view.find_all("tbody", ["boxShadow"])

        result_1 = result_view_rows[0].find("tr", ["firstrow"])
        result_2 = result_view_rows[1].find("tr", ["firstrow"])
        result_3 = result_view_rows[2].find("tr", ["firstrow"])

        time_1 = result_1.find("td", ["time"]).decode_contents().split()[0]
        duration_1 = result_1.find(
            "td", ["duration lastrow"]).decode_contents().split()[0]
        time_2 = result_2.find("td", ["time"]).decode_contents().split()[0]
        duration_2 = result_2.find(
            "td", ["duration lastrow"]).decode_contents().split()[0]
        time_3 = result_3.find("td", ["time"]).decode_contents().split()[0]
        duration_3 = result_3.find(
            "td", ["duration lastrow"]).decode_contents().split()[0]
        return [
            {"time": time_1, "duration": duration_1},
            {"time": time_2, "duration": duration_2},
            {"time": time_3, "duration": duration_3}]
