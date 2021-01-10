import requests
import smtplib
import os
from twilio.rest import Client

# Twilio account details:
account_sid = "ACCOUNT_SID"
auth_token = os.environ.get("AUTH_TOKEN")
sms_from = os.environ.get("SMS_FROM")
sms_to = os.environ.get("SMS_to")

# Email account details:
my_user = os.environ.get("MY_EMAIL")
my_pass = os.environ.get("MY_PASS")

# Open Weather account details:
api_key = os.environ.get("OMW_API_KEY")
parameters = {
    "appid": api_key,
    "lat": "55.755825",
    "lon": "37.617298",
    "exclude": "current, minutely, hourly"
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
weather_slice = weather_data["daily"][:1]

# Loop through every id in weather list:
will_rain = False

for hour_data in weather_slice:
    # TODO fetch weather id from hourly list:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

    if will_rain:
        # Send SMS:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="Its going to rain now!",
            from_=os.environ.get("SMS_FROM"),
            to=os.environ.get("SMS_to")
        )
        # Check if sms was successfully sent:
        print(message.status)
        print("\n")

        # Send Email:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(
                user=my_user,
                password=my_pass
            )
            connection.sendmail(
                from_addr=my_user,
                to_addrs="tareq.joudeh@gmail.com",
                msg="Subject: It's going to rain!\n\n Rainy day today! let it rain!\n Tareq Pythoneer".encode("utf8")
            )
        print("Bring an umbrella")
    else:
        print("Sunny day today!")

 