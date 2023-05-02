import requests 

class CountryAPI: 
    def __init__(self, name): 
        self.name = name
        self.url = f"https://restcountries.com/v2/name/{name}?fullText=true"
        self.data = self.get()

    def get(self):
        response = requests.get(self.url)
        if response.status_code == 200: 
            data = response.json()[0]
            return data
        else: 
            raise Exception("Error finding country data")
        
    


    
        





