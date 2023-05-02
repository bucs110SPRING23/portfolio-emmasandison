import requests 

class CountryAPI: 
    def __init__(self, country_name): 
        self.country_name = country_name

    def get(self):
        url = f"https://restcountries.com/v2/name/{self.country_name}?fullText=true"
        response = requests.get(url)
        if response.status_code == 200: 
            data = response.json()
            if data: 
                return data[0]["alpha2Code"]
        return None

    
        





