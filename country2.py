import requests
from bs4 import BeautifulSoup
import random

# Set the country to search for addresses
country = "United States"

# Fetch the list of states for the given country
response = requests.get(f"https://www.travelmath.com/{country}/states")
soup = BeautifulSoup(response.text, "html.parser")
state_links = soup.select("#content a")
states = [link.text for link in state_links]

# Pick a random state from the list
state = random.choice(states)

# Fetch a random address from the state
response = requests.get(f"https://www.travelmath.com/random-street/{state}")
soup = BeautifulSoup(response.text, "html.parser")
address_span = soup.select_one(".rand_text")

if address_span is not None:
    address = address_span.text.strip()
    # Print the random address
    print(f"Random address in {state}, {country}: {address}")
else:
    print(f"No random address found for {state}, {country}")
