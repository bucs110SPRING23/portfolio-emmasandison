from country_api import CountryAPI
from timezone_api import TimezoneAPI


def main(): 
    city_name = input("Enter a city name: ").lower().strip()

    country = CountryAPI(city_name)
    if not country.data: 
        print(f"No data found for {city_name}")
        return 
    
    timezone = TimezoneAPI(city_name)
    time = timezone.get()
    
    if time:
        print(f"The current date and time in {city_name.title()} is {time}")
    else: 
        print(f"No data found for {city_name.title()}")
 

main()

