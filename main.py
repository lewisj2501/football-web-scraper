# working from branch lewis

import requests
import html
from bs4 import BeautifulSoup

# create the URL to the page you want to scrape
url = 'https://www.worldfootball.net/players_list/eng-premier-league-2022-2023/nach-mannschaft/1/'

# Make the http request to worldfootball.net
response = requests.get(url)

# parse the response
soup = BeautifulSoup(response.text, 'html.parser')

# finds table class with meta data associated with all the teams in the premier league
column_headers = soup.find_all("th")
row_data = soup.find_all('table', class_='standard_tabelle')

# Check the status code to make sure the request was successful
if response.status_code == 200:
    for row in row_data:
        data = row.text.split()
        col1 = data[0]
        col2 = data[1]
        col3 = data[2]
        col4 = data[3]
        col5 = data[4]
        print(data)
        print('break')

else:
    print("Request failed with status code:", response.status_code)
