# if you dont have beautifulsoup
# use: pip install beautifulsoup4

# if you don't have access to requests you can try
# use: pip install requests

import requests
from bs4 import BeautifulSoup

country = input("Enter Country Name (EX: USA): ")

city = input("Enter City Name: ")
city_formatted = city.lower().replace(" ", "-")

url = f"https://www.timeanddate.com/weather/{country}/{city_formatted}"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

try:
    temperature = soup.find("div", class_="h2").get_text(strip=True)
    description = soup.find("div", class_="h2").find_next("p").get_text(strip=True)

    print(f"Weather in {country}, {city}: ")
    print(f"Temperature: {temperature}")
    print(f"Condition: {description}")

except AttributeError:
    print("Please check the country and/or city name and try again.")


