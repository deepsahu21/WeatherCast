import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

if not api_key:
    print("Warning: API_KEY environment variable is not set")

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int



     
def get_lat_lon(city_name, state_code, country_code, API_key):
    if not API_key:
        raise ValueError("API_KEY is not set")
    try:
        resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
        if not resp or len(resp) == 0:
            raise ValueError("Location not found")
        data = resp[0]
        lat, lon = data.get('lat'), data.get('lon')
        if lat is None or lon is None:
            raise ValueError("Invalid location data")
        return lat, lon
    except requests.RequestException as e:
        raise ValueError(f"Error fetching location: {e}")
    
def get_current_weather(lat, lon, API_key):
    if not API_key:
        raise ValueError("API_KEY is not set")
    try:
        resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=imperial').json()
        if 'cod' in resp and resp['cod'] != 200:
            raise ValueError(f"Weather API error: {resp.get('message', 'Unknown error')}")
        if 'weather' not in resp or len(resp.get('weather', [])) == 0:
            raise ValueError("Invalid weather data received")
        if 'main' not in resp:
            raise ValueError("Invalid weather data received")
        data = WeatherData(
            main = resp.get('weather')[0].get('main'),
            description = resp.get('weather')[0].get('description'),
            icon = resp.get('weather')[0].get('icon'),
            temperature= int(resp.get('main').get('temp'))
        )
        return data
    except requests.RequestException as e:
        raise ValueError(f"Error fetching weather: {e}")

def main(city_name=None, state_name=None, country_name=None, lat=None, lon=None):
    if lat != None and lon != None:
        weather_data = get_current_weather(lat, lon, api_key)
        return weather_data
    elif city_name != None and state_name != None and country_name != None:
        lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
        weather_data = get_current_weather(lat, lon, api_key)
        return weather_data
    else:
        return None  # Or handle the error as you see fit
if __name__ == '__main__':
    lat, lon = get_lat_lon('Toronto', 'ON', 'Canada', api_key)
    print(get_current_weather(lat, lon, api_key))



    
