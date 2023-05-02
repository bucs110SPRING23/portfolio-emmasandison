import requests 

class LocationAPI: 
    def __init__(self, city): 
        self.city = city
        self.url = f"https://api.opencagedata.com/geocode/v1/json?q={self.city}&key=47255ad0d38641cf960e07579964e7f9"
        self.data = self.get()

    def get(self):
        response = requests.get(self.url)
        if response.status_code == 200: 
            data = response.json()
            if data["total_results"] > 0: 
                return data["results"][0]["geometry"]
        return None
        