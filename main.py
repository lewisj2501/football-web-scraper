# working from branch lewis

import requests
from bs4 import BeautifulSoup

# create the URL to the page you want to scrape
url = 'https://www.worldfootball.net/players_list/eng-premier-league-2022-2023/nach-mannschaft/1/'

# Make the http request to worldfootball.net
response = requests.get(url)

# parse the response
soup = BeautifulSoup(response.text, 'html.parser')

# finds table class with meta data associated with all the teams in the premier league
teamsList_1 = soup.find_all(class_ = "standard_tabelle")

# Make the http request to worldfootball.net

# Check the status code to make sure the request was successful
if response.status_code == 200:
    for team1 in teamsList_1:
        print(team1)
else:
    print("Request failed with status code:", response.status_code)
