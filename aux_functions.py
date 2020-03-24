import os
import pandas as pd
import numpy as np
import smtplib

sender_email = 'coronavirusupdates2910@gmail.com'
sender_pw = 'Covid19Coronavirus'

def email_sender(rcv_name, rcv_email, country, subject, body):
    global sender_email
    global sender_pw  

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(sender_email, sender_pw)

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(sender_email, rcv_email, msg)
        print('Email has been sent to ' + rcv_email)

        server.quit()

    except Exception as e:
        print(e)

def send_welcome_mail(rcv_name, rcv_email, country):

    subject = 'Welcome to Coronavirus Updates!'

    info = get_details_of(country)

    body = 'Hi ' + rcv_name + ',\
        \nToday in ' + country + '\
        \nTotal cases: ' + str(info[0]) +'\
        \nNew cases: ' + str(info[1]) + '\
        \nTotal deaths: ' + str(info[2]) + '\
        \nNew deaths: ' + str(info[3]) + '\
        \nTotal Recovered: ' + str(info[4]) + '\
        \nActive Cases: ' + str(info[5]) + '\
        \nSerious and critical cases: ' + str(info[6])  + '\
        \nTotal cases per million people: ' + str(info[7]) + '\
        \nYou will now recieve regular updates about Coronavirus from us!'

    email_sender(rcv_name, rcv_email, country, subject, body)

def send_regular_mail(rcv_name, rcv_email, country):

    subject = 'Coronavirus stats in your country today!'

    info = get_details_of(country)

    body = 'Hi ' + rcv_name + ',\
        \nToday in ' + country + '\
        \nTotal cases: ' + str(info[0]) +'\
        \nNew cases: ' + str(info[1]) + '\
        \nTotal deaths: ' + str(info[2]) + '\
        \nNew deaths: ' + str(info[3]) + '\
        \nTotal Recovered: ' + str(info[4]) + '\
        \nActive Cases: ' + str(info[5]) + '\
        \nSerious and critical cases: ' + str(info[6])  + '\
        \nTotal cases per million people: ' + str(info[7])

    email_sender(rcv_name, rcv_email, country, subject, body)

def get_details_of(country):
    abs_file_path = os.path.abspath(__file__)
    csv_file_path = abs_file_path.replace(abs_file_path.split('/')[-1], '') + 'corona_details.csv'
    print(csv_file_path)
    df = pd.read_csv(csv_file_path)
    req = df.loc[df['Country,Other'].str.lower() == country.lower()]
    vals = list(req.to_dict(orient='records')[0].values())
    vals = list(map(convert_to_int, vals[1:]))
    print(vals)
    return vals

def convert_to_int(string):
    # string hai to ye
    try:
        string = string.strip()
        if string == '':
            return 0
    except:
        pass
    try:
        string = string.replace(',', '')
    except:
        pass
    try:
        string = string.replace('+', '')
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
