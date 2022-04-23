from dotenv import load_dotenv
import requests
import os
from urllib.error import HTTPError

from constants import BASE_URL

load_dotenv()

# if you don't have .env file you can put YELP API key here
token = ''
BEARER_TOKEN = os.getenv('BEARER_TOKEN', token)


class SearchAPI(object):

    def __init__(self):
        self.headers = {
            'Authorization': f'Bearer {BEARER_TOKEN}',
        }

    def search_by_location(self, location):
        url = f"{BASE_URL}" + f"&location={location}"
        try:
            response = requests.request("GET", url, headers=self.headers)
            parsed_list = self._parse_location_response(response)
            status = 0
        except HTTPError:
            parsed_list = []
            status = 1
        return status, parsed_list

    def _parse_location_response(self, response):
        taco_bell_list = []
        r_json = response.json()
        biz = r_json.get('businesses')
        if not biz:
            return taco_bell_list
        for b in biz:
            # other taco resturants show up in search so filter them out, as well as closed resturants
            if b.get('name') == 'Taco Bell' and b.get('is_closed') == False:
                phone = b.get('display_phone')
                location = b.get('location')
                address = location.get('display_address')
                taco_bell_list.append({'address': address, 'phone': phone })
        return taco_bell_list
