from country_api import CountryAPI
from timezone_api import TimezoneAPI
from geocoding_api import GeocodingAPI


def main(): 
    location = input("Enter a location (city or country): ").lower().strip()

    geocoding = GeocodingAPI(city)
    lat, lng = geocoding.get_lat_lng()

    if not lat or not lng: 
        print(f"No location found")

    country = CountryAPI(lat, lng)
    city = geocoding.get_city_name()
    
    timezone = TimezoneAPI(lat, lng)
    time = timezone.get()
    
    if time:
        print(f"The current date and time in {city.title()}, {country.title()} is {time}")
    else: 
        print(f"No data found for {city.title()}, {country.title()}")
 

main()

