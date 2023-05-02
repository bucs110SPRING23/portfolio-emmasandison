import requests 

class LocationAPI: 
    def __init__(self, name): 
        self.name = name
        self.url = f"https://restcountries.com/v3.1/name/{name}?fullText=true"
        self.data = self.get()

    def get(self):
        response = requests.get(self.url)
        if response.status_code == 200: 
            data = response.json()[0]
            return data
        