import requests

parameters = {
    "appid": "e101304296b777bf49aa00d70e2301da",
    "lat": "48.135124",
    "lon": "11.581981",
    "exclude": "current, minutely, hourly"
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall",
    params=parameters
)
print(f"Server response: {response.status_code}")
print("\n")
response.raise_for_status()

weather_data = response.json()

weather_slice = weather_data["daily"][:10]

is_rain = False

for index, daily_data in enumerate(weather_slice):
    condition_id = daily_data["weather"][0]["id"]
    if condition_id < 700:
        is_rain = True

    if is_rain:
        print(index, "Rain")
    else:
        print(index, "Sunny")
