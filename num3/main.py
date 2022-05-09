import re
import requests


class Maper:

    def __init__(self):
        self.host = 'https://geocode-maps.yandex.ru/1.x/'

    def create_map(self, query):
        params_query_get = {
            'apikey': '1a78dda4-1157-4234-8cfa-8624cb129414',
            'geocode': query,
            'format': 'json'
        }

        resp = requests.get(self.host, params=params_query_get)
        response = resp.json()

        if response['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found'] == '0':
            return False

        resp_static = requests.get('https://static-maps.yandex.ru/1.x/?ll=' +
                                   re.sub(r"\s", r",",
                                          response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"][
                                              "Point"][
                                              "pos"])
                                   + '&spn=0.016457,0.00619&l=map')

        with open('static/img/map.png', 'wb') as f:
            f.write(resp_static.content)
        return True
