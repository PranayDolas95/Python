import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "2aa6a4c6d4aea098dd63c6ecd3d080bd"
CITY =  str(input("Enter City name : "))

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenhiet = celsius * (9/5) + 32
    return celsius, fahrenhiet     


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit} °F")
print(f"Temperature in {CITY}feels_like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit} °F") 
print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit} °F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"General Weather in {CITY}: {description}")
print(f"Sun rises in {CITY}:{sunrise_time}local time.")
print(f"Sun sets in {CITY}:{sunset_time}local time.")








