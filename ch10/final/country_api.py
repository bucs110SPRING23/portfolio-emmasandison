import requests 

class CountryAPI: 
    def __init__(self, lat, lng): 
        self.lat = lat 
        self.lng = lng
        self.url = f"https://api.opencagedata.com/geocode/v1/json?q={self.lat}+{self.lng}&key=47255ad0d38641cf960e07579964e7f9"

        self.data = self.get()

    def get(self):
        response = requests.get(self.url)
        if response.status_code == 200: 
            data = response.json()["results"][0]["components"]
            country = data["country"]
            return country
        
    
       
    
