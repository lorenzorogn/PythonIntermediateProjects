import requests

api_key = "c68a87f9c93d79206345b005f1c01a4f"

url = "https://api.openweathermap.org/data/2.5/weather"

weather_params = {
    "lat": 44.34,
    "lon": 10.99,
    "appid": api_key
}

response = requests.get(url, params=weather_params)
response.raise_for_status()

wheater_data = response.json()