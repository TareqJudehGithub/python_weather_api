import requests

parameters = {
    "appid": "e101304296b777bf49aa00d70e2301da",
    "lat": "31.945368",
    "lon": "35.928371",
    "exclude": "current, minutely, daily"
}
response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall",
    params=parameters
)
print("\n")
print(f"Response: {response.status_code}")
response.raise_for_status()
weather_data = response.json()

# Challenge: print out "Bring an umbrella" if any of the next 12 hours
# weather condition codes is less than 700

# TODO weather forecast for only the next 12 hours:
weather_slice = weather_data["hourly"][:12]

# Loop through every id in weather list:
will_rain = False

for hour_data in weather_slice:
    # TODO fetch weather id from hourly list:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

    if will_rain:
        print("Bring an umbrella")
    else:
        print("Today it's sunny!")







