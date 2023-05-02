from country_api import CountryAPI
from timezone_api import TimezoneAPI


def main(): 
    country_name = input("Enter a country name: ").lower().strip()

    country = CountryAPI(country_name)
    if not country.data: 
        print(f"No data found for {country_name}")
        return
    
    city = input("Enter a city of the country: ").lower().strip()

    timezone = TimezoneAPI(city)
    time = timezone.get()
    
    if time:
        print(f"The current date and time in {city.title()}, {country_name.title()} is {time}")
    else: 
        print(f"No data found for {city.title()}, {country_name.title()}")
 

main()

