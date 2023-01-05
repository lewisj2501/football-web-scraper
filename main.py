# working from branch lewis

import requests
from bs4 import BeautifulSoup

# create the URL to the page you want to scrape
url = 'https://www.worldfootball.net/'

# Make the http request to worldfootball.net
response = requests.get(url)

print(response)

# parse the response
soup = BeautifulSoup(response.text, 'html.parser')

# Make the http request to worldfootball.net

# Check the status code to make sure the request was successful
if response.status_code == 200:
    print(soup)
else:
    print("Request failed with status code:", response.status_code)
