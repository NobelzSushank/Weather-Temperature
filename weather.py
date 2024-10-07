import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def get_current_weather():
    print("\n*** Get current weather conditions ***\n")

    city = input("\n Please enter a city name: \n")

    request_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(request_url)

    weather_data = requests.get(request_url).json()

    # pprint(weather_data)
    print(f"Current wheather for {weather_data['name']}")
    print(f"The temp is {weather_data['main']['temp']}")
    print(f"Feels Like {weather_data['main']['feels_like']} and {weather_data['weather'][0]['description']}")


if __name__ == "__main__":
    get_current_weather()