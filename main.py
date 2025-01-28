import requests
# import psycopg2
# from datetime import datetime
import pandas as pd
import os

df = pd.read_excel('cities_list.xlsx')

df.rename(columns={"name": "City", "lon": "Longitude", "lat": "Latitude", "country": "Country"}, inplace=True)

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    print("API key not founded")

df_pollution = pd.DataFrame(data=df, index=None, columns=df.columns)

def get_air_pollution_Data(API_KEY, lat, lon):
    
    url = f'http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error requisition: {response.status_code}')
        return None
    
lat = '40.7128'
lon = '-74.0060'

data = get_air_pollution_Data(API_KEY, lat, lon)