import requests 
from datetime import datetime, timedelta

class TimezoneAPI: 
    def __init__(self, timezone): 
        self.timezone = timezone

    def get(self): 
        url = f"http://worldtimeapi.org/api/timezone/{self.timezone}"
        response = requests.get(url)
        if response.status_code == 200: 
            data = response.json()
            time_str = data['datetime']
            time = datetime.fromisoformat(time_str[:-1])
            offset = timedelta(seconds=data["raw_offset"] + data["dst_offset"])
            return time + offset
        else: 
            raise Exception("No data for timezone")
