import requests

class LocationAPI:
    def __init__(self):
        self.url = "https://restcountries.com/v3.1/name/{country}?fullText=true"

    def get_capital_city(self, country_name):
        response = requests.get(self.url.format(country=country_name))
        if response.status_code == 200:
            data = response.json()
            capital_city = data[0]["capital"]
            return capital_city
        else:
            return None