import requests 

class SportsAPI: 
    def __init__(self, country_code): 
        self.country_code = country_code

    def get(self): 
        url = f"https://www.thesportsdb.com/api/v1/json/1/search_all_leagues.php?c={self.country_code}"
        response = requests.get(url)
        if response.status_code == 200: 
            data = response.json()
            if data["countries"]: 
                return data["countries"][0]["strSport"]
        return None
