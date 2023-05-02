from country_api import CountryAPI
from sport_api import SportsAPI


def main(): 
    country_name = input("Enter a country name: ")

    country = CountryAPI(country_name)
    country_code = country.get_country_code()

    if country_code: 
        sport = SportsAPI(country_code)
        most_popular_sport = sport.get_most_popular_sport()
        if most_popular_sport: 
            print(f"The most popular sport in {country_name} is {most_popular_sport}")
        else: 
            print(f"No popular sports found for {country_name}")
    else: 
        print(f"Country code not found for {country_name}")

main()