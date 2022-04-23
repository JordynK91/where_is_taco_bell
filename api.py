import requests
from urllib.error import HTTPError

from constants import BASE_URL

load_dotenv()



class SearchAPI(object):

    def __init__(self, token):
        self.headers = {
            'Authorization': f'Bearer {token}',
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
