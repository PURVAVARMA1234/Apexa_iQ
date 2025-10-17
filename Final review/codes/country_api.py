#This script fetches and displays information about a country using the REST Countries API.
# It prompts the user for a country name and retrieves details like capital, population, currency, languages, and flag.


import requests

country_name = input("Enter a country name (e.g., 'United States', 'Japan'): ")


api_url = f"https://restcountries.com/v3.1/name/{country_name}?fields=name,capital,population,currencies,languages,flags"


response = requests.get(api_url)


if response.status_code == 200:
    
    countries = response.json()

    if countries:  
        country = countries[0] 
        name = country['name']['common']
        capital = country['capital'][0] if country['capital'] else "No capital listed"
        population = f"{country['population']:,}" 
        currencies = list(country['currencies'].keys())[0] if country['currencies'] else "N/A"
        languages = ", ".join(country['languages'].values()) if country['languages'] else "N/A"
        flag_url = country['flags']['png'] 

        
        print(f"\nHere's info on {name} from the REST Countries API:")
        print(f"- Capital: {capital}")
        print(f"- Population: {population}")
        print(f"- Currency: {currencies}")
        print(f"- Languages: {languages}")
        print(f"- Flag: {flag_url} (you can open this URL in a browser)")
    else:
        print("No country found with that name. Try exact spelling (e.g., 'Germany').")#to print else statement
else:
      print(f"Error: Couldn't fetch data (code: {response.status_code}). Check your internet.")


print("\nDone! This fetched real country data from a professional REST API.")