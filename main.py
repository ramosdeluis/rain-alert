import os
import requests
from twilio.rest import Client

TWILIO_ACCOUNT_SID: str
TWILIO_AUTH_TOKEN: str
API_KEY = ''
TWILIO_ACCOUNT_SID=''
TWILIO_AUTH_TOKEN=''
LAT = -27.577278
LNG = -48.525576
LOCATION_KEY = 35952
LOCATION_KEY_two = 39340

OWM_Endpoint = f'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{LOCATION_KEY_two}'

weather_params = {
    'lat': LAT,
    'lon': LNG,
    'apikey': API_KEY,
    'language': 'en-us',
    'details': False,
    'metric': False

}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

data = response.json()

probably_rain: bool = False


def is_rain_12_hours(my_data: list) -> None:
    global probably_rain
    for hour in my_data:
        if hour['PrecipitationProbability'] >= 60:
            probably_rain = True


is_rain_12_hours(data)

if probably_rain:
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_='+14245005133',
        to='+99999999999'
    )

    print(message.status)
