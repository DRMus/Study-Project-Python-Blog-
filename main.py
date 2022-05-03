import re

import requests

query = input('Введите город: ')

host = 'https://geocode-maps.yandex.ru/1.x/'

params_query_get = {
    'apikey': '',
    'geocode': query,
    'format': 'json'
}
resp = requests.get(host, params=params_query_get)
response = resp.json()

resp_static = requests.get('https://static-maps.yandex.ru/1.x/?ll=' +
                           re.sub(r"\s", r",",
                                  response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"][
                                      "pos"])
                           + '&spn=0.016457,0.00619&l=map')

print(resp_static.status_code)

with open('map.png', 'wb') as f:
    f.write(resp_static.content)
