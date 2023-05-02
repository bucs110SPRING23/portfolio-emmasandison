from country_api import CountryAPI
from timezone_api import TimezoneAPI


def main(): 
    country_name = input("Enter a country name: ").lower().strip()

    country = CountryAPI(country_name)
    timezone = country.data["timezones"][0]
    timezone_api = TimezoneAPI(timezone)
    time = timezone_api.get()

    if time:
        print(f"The current time in {country_name} is {time}")
    else: 
        print(f"No data found for {country_name}")
    
main()