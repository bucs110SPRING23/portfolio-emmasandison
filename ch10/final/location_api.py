import requests

class LocationAPI:
    def __init__(self):
        """
        This function defines the __init__ method and initializes the url as an instance of LocationAPI
        """
        self.url = "https://restcountries.com/v3.1/name/{country}?fullText=true"

    def get_capital_city(self, country_name):
        """
        This function is sending a GET request to the REST countries API to find the capital city of the given country
        returns capital city 
        """
        response = requests.get(self.url.format(country=country_name))
        if response.status_code == 200:
            data = response.json()
            capital_city = data[0]["capital"][0]
            return capital_city
        else:
            return None