# working from branch work
import requests
import html
from bs4 import BeautifulSoup

import csv

header = ['Player', 'Team', 'Born', 'Height', 'Position']
cell = []

for x in range(14):

    counter = x + 1
    # create the URL to the page you want to scrape
    url = 'https://www.worldfootball.net/players_list/eng-premier-league-2022-2023/nach-mannschaft/' + str(counter) + '/'

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
            currentData = []
            data = row.text.split()
            col1 = str(data[5]) + str(data[6])
            currentData.append(col1)
            col2 = str(data[7]) + str(data[8])
            currentData.append(col2)
            col3 = data[9]
            currentData.append(col3)
            col4 = str(data[10]) + str(data[11])
            currentData.append(col1)
            col5 = data[12]
            currentData.append(col2)
            print(data)
            print('break')
            cell.append(currentData)

    else:
        print("Request failed with status code:", response.status_code)

with open('c:/Users/Admin/dump/players.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)
    writer.writerow(cell)
    # close the file
    f.close()
