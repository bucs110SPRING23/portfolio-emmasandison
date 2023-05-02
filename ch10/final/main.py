from location_api import LocationAPI
from weather_api import WeatherAPI


def main(): 
    country_name = input("Enter a country name: ").lower().strip()

    location_api = LocationAPI()
    capital_city = location_api.get_capital_city(country_name)

    if capital_city is not None: 
        weather_api = WeatherAPI(api_key="ddaf354d5eac5539bc9dd3aedb088d86")
        temperature = weather_api.get(capital_city)

        if temperature is not None: 
            print(f"The capital of {country_name} is {capital_city}")
            print(f"The temperature in {capital_city} is {temperature} K")
        else: 
            print(f"No weather data for {capital_city}")
    else: 
        print(f"Error getting capital city for {country_name}")

main()

