import requests 
from datetime import datetime, timedelta

class TimezoneAPI: 
    def __init__(self, city): 
        self.city = city
        self.url = f"http://api.timezonedb.com/v2.1/get-time-zone?key=LN6DJUMQBB0Z&format=json&by=position&lat=0&lng=0&city={self.city}"

    def get(self): 
        response = requests.get(self.url)
        if response.status_code == 200: 
            data = response.json()
            time_str = data["formatted"]
            time = datetime.fromisoformat(time_str)
            offset = timedelta(seconds=data["gmtOffset"])
            local_time = time + offset
            return local_time
        
    def get_local_time(self): 
        local_time = self.get()
        if local_time: 
            formatted_time = local_time.strftime("%I:%M:%S %p")
            return formatted_time
       