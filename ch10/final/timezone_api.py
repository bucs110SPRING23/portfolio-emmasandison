import requests 
from datetime import datetime, timedelta

class TimezoneAPI: 
    def __init__(self, lat, lng): 
        self.lat = lat
        self.lng = lng
        self.url = f"https://api.timezonedb.com/v2.1/get-time-zone?key=LN6DJUMQBB0Z&format=json&by=position&lat={self.lat}&lng={self.lng}"

    def get(self): 
        response = requests.get(self.url)
        if response.status_code == 200: 
            data = response.json()
            time_str = data["formatted"]
            time = datetime.fromisoformat(time_str)
            offset = timedelta(seconds=data["gmtOffset"])
            local_time = time + offset
            return local_time.strftime("%I:%M:%S %p")
        
       