import requests
import psycopg2
from datetime import datetime
import os

API_KEY = os.getenv('API_KEY')

def get_air_pollution_Data(API_KEY, lat, lon):
    
    url = f'http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return print(f'Error requisition: {response.status_code}')
    
lat = '40.7128'
lon = '-74.0060'

data = get_air_pollution_Data(API_KEY, lat, lon)

columns = []

for i in data['list'][0]['components'].keys():
    columns.append(i)