import requests 

class WeatherAPI: 
    def __init__(self, api_key): 
        """
        This function is takes the api_key as a parameter and initializes it as an attribute of the WeatherAPI. This function also initializes the url as an attribute.
        """
        self.api_key = api_key
        self.url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}" 

    def get(self, city): 
        """
        This function is setting a GET request to the OpenWeatherMap API with a city and API key to find the temperature data in Kelvin
        returns temperature 
        """
        response = requests.get(self.url.format(city=city, api_key=self.api_key))
        if response.status_code == 200: 
            data = response.json()
            temperature = data["main"]["temp"]
            return temperature 
        else: 
            return None
        
    def kelvin_to_fahrenheit(self, kelvin_temp):
        """
        This function converts the Kelvin temperature returned in the get() function to Fahrenheit
        returns the fahrenheit temperature
        """
        fahrenheit_temp = (kelvin_temp - 273.15) * 1.8 + 32
        return fahrenheit_temp

        
