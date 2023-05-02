import requests 
from datetime import datetime, timedelta
from location_api import LocationAPI

class TimezoneAPI: 
    def __init__(self, lat, lng): 
        self.url = f"http://api.timezonedb.com/v2.1/get-time-zone?key=LN6DJUMQBB0Z&format=json&by=position&lat={lat}&lng={lng}"
    
    
    def get(self): 
        response = requests.get(self.url)
        if response.status_code == 200: 
            data = response.json()
            if "formatted" not in data: 
                print("Error: No time data found.")
                return None
            time_str = data["formatted"]
            time = datetime.fromisoformat(time_str)
            offset = timedelta(seconds=data["gmtOffset"])
            local_time = time + offset
            return local_time.strftime("%I:%M:%S %p")
        else: 
            print("No data found")
            return None

        
        
       