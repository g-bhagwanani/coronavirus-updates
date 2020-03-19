import pandas as pd
import numpy as np
import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen
import smtplib

sender_email = 'coronavirusupdates2910@gmail.com'
sender_pw = 'Covid19Coronavirus'

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

def send_mail(reciever_email, country):
    global sender_email
    global sender_pw

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(sender_email, sender_pw)

    subject = 'Coronavirus stats in your country today!'

    info = get_details_of(country)

    body = 'xyz'

    body = 'Today in ' + country + '\
        \nThere is new data on coronavirus:\
        \nTotal cases: ' + str(info[0]) +'\
        \nNew cases: ' + str(info[1]) + '\
        \nTotal deaths: ' + str(info[2]) + '\
        \nNew deaths: ' + str(info[3]) + '\
        \nActive cases: ' + str(info[4]) + '\
        \nTotal recovered: ' + str(info[5]) + '\
        \nSerious, critical cases: ' + str(info[6])  + '\
        \nTotal cases per million: ' + str(info[7])

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(sender_email, ['gaurav.bhagwanani@gmail.com', 'karanidnani10@gmail.com'], msg)
    print('Hey Email has been sent!')

    server.quit()

# incomplete code!
def get_details_of(country):
    df = pd.read_csv('corona_details.csv')
    req = df.loc[df['Country,Other'].str.lower() == country.lower()]
    vals = list(req.to_dict(orient='records')[0].values())
    vals = list(map(convert_to_int, vals[1:]))
    print(vals)
    return vals

def convert_to_int(string):
    # string hai to ye
    try:
        string = string.replace(',', '')
    except:
        pass
    # NaN hai to ye
    try:
        if np.isnan(string):
            return 0
    except:
        pass
    try:
        return int(string)
    except ValueError:
        return float(string)

refresh_csv()
send_mail('g.bhagwanani@somaiya.edu', 'India')