from location_api import LocationAPI
from timezone_api import TimezoneAPI


def main(): 
    city_name = input("Enter a European city name: ").lower().strip()

    location = LocationAPI(city_name)
    if not location.data: 
        print(f"No data found for {city_name}")
        return 
    
    timezone = TimezoneAPI(city_name)
    time = timezone.get()
    
    if time:
        print(f"The current time in {city_name.title()} is {time}")
    else: 
        print(f"No data found for {city_name.title()}")
 

main()

