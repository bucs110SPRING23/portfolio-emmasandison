from location_api import LocationAPI
from weather_api import WeatherAPI


def main(): 
    country_name = input("Enter a country name: ").lower().strip()

    location_api = LocationAPI()
    capital_city = location_api.get_capital_city(country_name)

    if capital_city is not None: 
        weather_api = WeatherAPI(api_key="daa7d8bfee911e4322b7576661a696d0")
        temperature = weather_api.get(capital_city)

        if temperature is not None: 
            fahrenheit_temp = weather_api.kelvin_to_fahrenheit(temperature)
            print(f"The capital of {country_name} is {capital_city}")
            print(f"The temperature in {capital_city} is {fahrenheit_temp} F")
        else: 
            print(f"No weather data for {capital_city}")
    else: 
        print(f"Error getting capital city for {country_name}")

main()

