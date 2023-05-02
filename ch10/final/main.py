from location_api import LocationAPI
from timezone_api import TimezoneAPI
from geopy.geocoders import Nominatim


def main(): 
    geolocator = Nominatim(user_agent="my_app")
    city_name = input("Enter a city name: ").lower().strip()

    location = geolocator.geocode(city_name)
    if not location:
        print(f"No data found for {city_name}")
        return 
    
    lat, lng = location.latitude, location.longitude
    
    timezone = TimezoneAPI(lat, lng)
    time = timezone.get()
    
    if time:
        print(f"The current time in {location} is {time.strftime('%H:%M:%S')}")
    else:
        print(f"No time data found for {city_name}")

main()

