import requests


OWN_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "e78d2ed796e314e81a4bfe63407080cb"

weather_params = {
    "lat": 43.736439,
    "lon": -79.344994,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()["hourly"][:12]

will_rain = False

for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")

