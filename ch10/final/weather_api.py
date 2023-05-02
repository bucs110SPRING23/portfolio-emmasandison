import requests 

class WeatherAPI: 
    def __init__(self, api_key): 
        self.api_key = api_key
        self.url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}" 

    def get(self, city): 
        response = requests.get(self.url.format(city=city, api_key=self.api_key))
        if response.status_code == 200: 
            data = response.json()
            temperature = data["main"]["temp"]
            return temperature 
        else: 
            return None


        
