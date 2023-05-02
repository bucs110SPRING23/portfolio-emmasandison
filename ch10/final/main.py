from country_api import CountryAPI
from timezone_api import TimezoneAPI


def main(): 
    country_name = input("Enter a country name: ").lower().strip()
    country = CountryAPI(country_name)
    
    if country.data: 
        capital = input("Enter the capital city of the country: ").lower().strip()
        timezone = TimezoneAPI(country.data["capital"])
        time = timezone.get()
        
        if time: 
            print(f"The current time in {capital.title()} is {time}")
        else: 
            print(f"No data found for {capital.title()}")
    else: 
        print(f"No data found for {country_name.title()}")

main()

