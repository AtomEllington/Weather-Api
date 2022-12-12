import requests

api_key = "7d9628a27cedf4ed1eaf720b0b9e001b"

user_input = input("Enter a city: ")

weather_data = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&appid={api_key}")

weather = weather_data.json() ['weather'] [0]['main']
temp = weather_data.json()['main']['temp']

print(f"Today's weather is {weather} and the temperature is {temp}.")   