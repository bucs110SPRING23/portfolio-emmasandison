import requests 

class GeocodingAPI: 
    def __init__(self, location): 
        self.location = location 
        self.url = f"https://api.opencagedata.com/geocode/v1/json?q={self.location}&key=47255ad0d38641cf960e07579964e7f9"
        self.data = self.get()

    def get(self): 
        response = requests.get(self.url)
        if response.status_code == 200: 
            data = response.json()["results"][0]
            self.lat = data["geometry"]["lat"]
            self.lng = data["geometry"]["lng"]
            return data
    
    def get_lat_lng(self): 
        return (self.lat, self.lng) if self.data else (None, None)

    def get_city_name(self): 
        components = self.data["components"]
        if "city" in components: 
            return components["city"]
        elif "town" in components: 
            return components["town"]
        elif "village" in components: 
            return components["village"]
        else: 
            return ""



