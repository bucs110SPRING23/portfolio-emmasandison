from location_api import LocationAPI
from weather_api import WeatherAPI


def main(): 
    """
    The main function prompts the user to enter a country name and then it retrieves the capital city from the LocationAPI file and if it is found then it uses the WeatherAPI to retrieve the temperature in that location in Kelvin which is then converted to Fahrenheit. 
    Prints the result or an error message if information cannot be retrieved
    """
    country_name = input("Enter a country name: ").lower().strip()

    location_api = LocationAPI()
    capital_city = location_api.get_capital_city(country_name)

    if capital_city is not None: 
        weather_api = WeatherAPI(api_key="daa7d8bfee911e4322b7576661a696d0")
        temperature = weather_api.get(capital_city)

        if temperature is not None: 
            fahrenheit_temp = round(weather_api.kelvin_to_fahrenheit(temperature), 2)
            print(f"The capital of {country_name} is {capital_city}")
            print(f"The temperature in {capital_city} is {fahrenheit_temp} F")
        else: 
            print(f"No weather data for {capital_city}")
    else: 
        print(f"Error getting capital city for {country_name}")

main()

