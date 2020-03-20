import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

def refresh_csv():
    soup = BeautifulSoup(urlopen('https://www.worldometers.info/coronavirus/'), 'lxml')
    print('soup generated')

    table = soup.find('table', attrs={ "id" : "main_table_countries_today"})
    print('table found')

    rows = []

    header = [a.text for a in table.find_all('th')]
    print(header)

    for row in table.find_all('tr'):
        rows.append([val.text for val in row.find_all('td')])

    with open('./corona_details.csv', 'w') as f:
        print('csv file generated')
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

refresh_csv()