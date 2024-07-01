import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://www.cardekho.com/tata/punch-ev"

# Send a GET request to the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize variables
    vehicle_name = "Not Available"
    price_range = "Not Available"
    key_specs = []
    top_features = []

    # Scrape the vehicle name
    vehicle_name_tag = soup.find('h1')
    if vehicle_name_tag:
        vehicle_name = vehicle_name_tag.get_text(strip=True)

    # Scrape the price range
    price_range_tag = soup.find('div', class_='price')
    if price_range_tag:
        price_range = price_range_tag.get_text(strip=True)

    # Scrape key specifications
    specs_section = soup.find('div', class_='gsc_col-xs-12 gsc_col-md-12 gsc_col-sm-12 gsc_col-lg-12')
    if specs_section:
        specs_items = specs_section.find_all('li')
        for item in specs_items:
            key_specs.append(item.get_text(strip=True))

    # Scrape top features
    features_section = soup.find('div', class_='features')
    if features_section:
        features_items = features_section.find_all('li')
        for item in features_items:
            top_features.append(item.get_text(strip=True))

    # Print the scraped data
    print("Vehicle Name:", vehicle_name)
    print("Price Range:", price_range)
    print("Key Specifications:", key_specs)
    print("Top Features:", top_features)

else:
    print("Failed to retrieve the webpage")

