import pytest
import requests

# Определяем геолокацию моего дома
base_url1 = 'https://geocode-maps.yandex.ru/1.x/'
def test_operations1():
    query_params = {'format': 'json',
                'apikey': 'c5af769c-6691-4205-bf76-614c25b96425',
                'geocode': '76.899556, 43.236194'}

    geolocation = requests.get(base_url1, params=query_params)

    print(geolocation.text)
    print(geolocation.status_code)

    assert geolocation.status_code == 200

# Находим топ5 ближайших аптек
base_url2 = 'https://search-maps.yandex.ru/v1/'
# endpoint=""
def test_operation2():
    query_params = {'format': 'json',
                'apikey': '89e251df-dd9a-4341-8fc2-144f1aba4292',
                'text': 'аптека',
                'lang': 'ru_RU',
                'll': '76.899556, 43.236194',
                'spn': '0.01,0.01',
                'type': 'biz',
                'results': '5'}

    nearestPharm = requests.get(base_url2, params=query_params)

    print(nearestPharm.text)
    print(nearestPharm.status_code)

    assert nearestPharm.status_code == 200

# Проверяем аптеку по ее uri
# def test_operation3():
#     query_params = {'format': 'json',
#                 'apikey': 'c5af769c-6691-4205-bf76-614c25b96425',
#                 'uri': 'ymapsbm1://org?oid=1123046306'}
#     thePharm = requests.get(base_url1, params=query_params)

#     print(thePharm.text)
#     print(thePharm.status_code)
#     pharm_info = thePharm.json()
#     assert pharm_info['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['name'] == 'Биосфера'
#     assert thePharm.status_code == 200
