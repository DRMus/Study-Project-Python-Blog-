import requests

resp = requests.get('https://static-maps.yandex.ru/1.x/?ll=37.677751,55.757718&spn=0.016457,0.00619&l=map')

print(resp.status_code)

with open('map.png', 'wb') as f:
    f.write(resp.content)
