import requests
import json
import os
from datetime import datetime, timedelta


script_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(script_dir, 'config.json')
cache_file = os.path.join(script_dir, 'data.json')

with open(config_file, 'r') as f:
    config = json.load(f)
    api_key = config['api_key']
    city = config['city']

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

def get_weather_data():
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        weather_data['lastRequested'] = datetime.now().isoformat()
        with open(cache_file, 'w') as f:
            json.dump(weather_data, f)
        return weather_data
    else:
        return None

if os.path.exists(cache_file):
    with open(cache_file, 'r') as f:
        try:
            cached_data = json.load(f)
            last_requested_str = cached_data.get('lastRequested')
            if last_requested_str:
                last_requested = datetime.fromisoformat(last_requested_str)
                if datetime.now() - last_requested < timedelta(minutes=30):
                    print(json.dumps(cached_data))
                else:
                    new_data = get_weather_data()
                    if new_data:
                        print(json.dumps(new_data))
                    else:
                        print(json.dumps(cached_data)) # fallback to cached data if API fails
            else:
                new_data = get_weather_data()
                if new_data:
                    print(json.dumps(new_data))
        except json.JSONDecodeError:
            new_data = get_weather_data()
            if new_data:
                print(json.dumps(new_data))
else:
    new_data = get_weather_data()
    if new_data:
        print(json.dumps(new_data))
