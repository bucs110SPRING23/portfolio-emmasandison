import requests 
from datetime import datetime, timedelta
from location_api import LocationAPI

class TimezoneAPI: 
    def __init__(self, city): 
        self.city = city
        self.location = LocationAPI(city).data

        if not self.location: 
            raise ValueError(f"No location data found for {city}")
        
        self.url = f"http://api.timezonedb.com/v2.1/get-time-zone?key=LN6DJUMQBB0Z&format=json&by=position&lat={self.location['lat']}&lng={self.location['lng']}"
    
    
    def get(self): 
        response = requests.get(self.url)
        if response.status_code == 200: 
            data = response.json()
            time_str = data["formatted"]
            time = datetime.fromisoformat(time_str)
            offset = timedelta(seconds=data["gmtOffset"])
            local_time = time + offset
            return local_time.strftime("%I:%M:%S %p")
        
       