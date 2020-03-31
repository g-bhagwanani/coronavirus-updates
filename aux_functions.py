import os
import pandas as pd
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import local_settings

sender_email = local_settings.official_email
sender_pw = local_settings.official_pw
website_url = local_settings.website_url

list_of_countries = ['China', 'Italy', 'Spain', 'Iran', 'Germany', 'USA', 'France', 'S. Korea', 'Switzerland', 'UK', 'Netherlands', 'Austria', 'Belgium', 'Norway', 'Sweden', 'Denmark', 'Malaysia', 'Portugal', 'Japan', 'Canada', 'Australia', 'Czechia', 'Diamond Princess', 'Israel', 'Brazil', 'Ireland', 'Pakistan', 'Greece', 'Luxembourg', 'Qatar', 'Finland', 'Chile', 'Poland', 'Iceland', 'Singapore', 'Indonesia', 'Ecuador', 'Turkey', 'Slovenia', 'Thailand', 'Romania', 'Bahrain', 'Estonia', 'Saudi Arabia', 'Egypt', 'Hong Kong', 'Russia', 'India', 'Peru', 'Philippines', 'South Africa', 'Iraq', 'Mexico', 'Lebanon', 'Kuwait', 'Colombia', 'San Marino', 'UAE', 'Panama', 'Slovakia', 'Armenia', 'Taiwan', 'Bulgaria', 'Argentina', 'Croatia', 'Serbia', 'Latvia', 'Uruguay', 'Vietnam', 'Algeria', 'Costa Rica', 'Hungary', 'Faeroe Islands', 'Brunei ', 'Andorra', 'Cyprus', 'Morocco', 'Sri Lanka', 'Dominican Republic', 'Albania', 'North Macedonia', 'Belarus', 'Jordan', 'Bosnia and Herzegovina', 'Moldova', 'Malta', 'Tunisia', 'Kazakhstan', 'Cambodia', 'Lithuania', 'Oman', 'Palestine', 'Guadeloupe', 'Azerbaijan', 'Georgia', 'Venezuela', 'Burkina Faso', 'New Zealand', 'Senegal', 'Uzbekistan', 'Martinique', 'Liechtenstein', 'Réunion', 'Ukraine', 'Afghanistan', 'Honduras', 'Bangladesh', 'Cameroon', 'DRC', 'Macao', 'Cuba', 'Jamaica', 'Bolivia', 'Ghana', 'Guyana', 'French Guiana', 'Guam', 'Maldives', 'Montenegro', 'Paraguay', 'Guatemala', 'Nigeria', 'Mauritius', 'Monaco', 'Channel Islands', 'French Polynesia', 'Rwanda', 'Gibraltar', 'Ivory Coast', 'Ethiopia', 'Togo', 'Trinidad and Tobago', 'Puerto Rico', 'Kenya', 'Seychelles', 'Equatorial Guinea', 'Kyrgyzstan', 'Mayotte', 'Mongolia', 'Tanzania', 'Aruba', 'Barbados', 'Saint Martin', 'Suriname', 'Cayman Islands', 'Curaçao', 'Gabon', 'Bahamas', 'CAR', 'Congo', 'Namibia', 'St. Barth', 'U.S. Virgin Islands', 'Sudan', 'Benin', 'Bermuda', 'Bhutan', 'Greenland', 'Guinea', 'Haiti', 'Isle of Man', 'Liberia', 'Mauritania', 'New Caledonia', 'Saint Lucia', 'Zambia', 'Nepal', 'Angola', 'Antigua and Barbuda', 'Cabo Verde', 'Chad', 'Djibouti', 'El Salvador', 'Fiji', 'Gambia', 'Vatican City', 'Montserrat', 'Nicaragua', 'Niger', 'Papua New Guinea', 'St. Vincent Grenadines', 'Sint Maarten', 'Somalia', 'Eswatini', 'World']

def email_sender(rcv_name, rcv_email, country, subject, html_body, text_body):
    global sender_email
    global sender_pw

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Coronavirus Updates <' + sender_email + '>'
    msg['To'] = rcv_email

    part1 = MIMEText(text_body, 'plain')
    part2 = MIMEText(html_body, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(sender_email, sender_pw)

        server.sendmail(sender_email, rcv_email, msg.as_string())
        print('Email has been sent to ' + rcv_email)

        server.quit()

    except Exception as e:
        print(e)

def send_welcome_mail(rcv_name, rcv_email, country):
    global website_url

    subject = 'Welcome to Coronavirus Updates!'

    info = get_details_of(country)

    html_body = """\
    <html>
        <head></head>
        <body>
            <p>Hi {}, <br></br> Today in {}, </p>
            <table style="border-style:solid; border-width:1px">
                <tbody>
                    <tr>
                        <td style="border-style:solid; border-width:1px">Total cases</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                    <tr>
                        <td style="border-style:solid; border-width:1px">New cases</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                    <tr>
                        <td style="border-style:solid; border-width:1px">Total deaths</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                    <tr>
                        <td style="border-style:solid; border-width:1px">New deaths</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                    <tr>
                        <td style="border-style:solid; border-width:1px">Total Recovered</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                    <tr>
                        <td style="border-style:solid; border-width:1px">Active Cases</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                    <tr>
                        <td style="border-style:solid; border-width:1px">Serious and critical cases</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                    <tr>
                        <td style="border-style:solid; border-width:1px">Total cases per million people</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                </tbody>
            </table>
            <p>For more information, please visit <a href="{}">our website</a></p>
            <p>You will now recieve regular coronavirus updates from us</p>
        </body>
    </html>
    """.format(rcv_name, country, str(info[0]), str(info[1]), str(info[2]), str(info[3]), str(info[4]), str(info[5]), str(info[6]), str(info[7]), website_url + ':3000/stats/' + country)

    text_body = 'Hi ' + rcv_name + ',\
        \nToday in ' + country + '\
        \nTotal cases: ' + str(info[0]) +'\
        \nNew cases: ' + str(info[1]) + '\
        \nTotal deaths: ' + str(info[2]) + '\
        \nNew deaths: ' + str(info[3]) + '\
        \nTotal Recovered: ' + str(info[4]) + '\
        \nActive Cases: ' + str(info[5]) + '\
        \nSerious and critical cases: ' + str(info[6])  + '\
        \nTotal cases per million people: ' + str(info[7]) + '\
        \nFor more information, please visit ' + website_url + ':3000/stats/' + country + '\
        \nYou will now recieve regular coronavirus updates from us!'

    email_sender(rcv_name, rcv_email, country, subject, html_body, text_body)

def send_regular_mail(rcv_name, rcv_email, country):

    subject = 'Coronavirus stats in your country today!'

    info = get_details_of(country)

    html_body = """\
    <html>
        <head></head>
        <body>
            <p>Hi {}, <br></br> Today in {}, </p>
            <table style="border-style:solid; border-width:1px">
                <tbody>
                    <tr>
                        <td style="border-style:solid; border-width:1px">Total cases</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                    <tr>
                        <td style="border-style:solid; border-width:1px">New cases</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                    <tr>
                        <td style="border-style:solid; border-width:1px">Total deaths</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                    <tr>
                        <td style="border-style:solid; border-width:1px">New deaths</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                    <tr>
                        <td style="border-style:solid; border-width:1px">Total Recovered</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                    <tr>
                        <td style="border-style:solid; border-width:1px">Active Cases</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                    <tr>
                        <td style="border-style:solid; border-width:1px">Serious and critical cases</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                    <tr>
                        <td style="border-style:solid; border-width:1px">Total cases per million people</td>
                        <td style="border-style:solid; border-width:1px">{}</td>
                    </tr>
                </tbody>
            </table>
            <p>For more information please visit <a href="{}">our website</a></p>
        </body>
    </html>
    """.format(rcv_name, country, str(info[0]), str(info[1]), str(info[2]), str(info[3]), str(info[4]), str(info[5]), str(info[6]), str(info[7]), website_url + ':3000/stats/' + country)

    text_body = 'Hi ' + rcv_name + ',\
        \nToday in ' + country + '\
        \nTotal cases: ' + str(info[0]) +'\
        \nNew cases: ' + str(info[1]) + '\
        \nTotal deaths: ' + str(info[2]) + '\
        \nNew deaths: ' + str(info[3]) + '\
        \nTotal Recovered: ' + str(info[4]) + '\
        \nActive Cases: ' + str(info[5]) + '\
        \nSerious and critical cases: ' + str(info[6])  + '\
        \nTotal cases per million people: ' + str(info[7]) + '\
        \nFor more information, please visit ' + website_url + ':3000/stats/' + country

    email_sender(rcv_name, rcv_email, country, subject, html_body, text_body)

def get_details_of(country):
    abs_file_path = os.path.abspath(__file__)
    csv_file_path = abs_file_path.replace(abs_file_path.split('/')[-1], '') + 'corona_details.csv'
    print(csv_file_path)
    df = pd.read_csv(csv_file_path)
    req = df.loc[df['Country,Other'].str.lower() == country.lower()]
    vals = list(req.to_dict(orient='records')[0].values())
    vals = list(map(convert_to_int, vals[1:-1]))
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

def get_history_of(country):
    abs_file_path = os.path.abspath(__file__)
    active_file_path = abs_file_path.replace(abs_file_path.split('/')[-1], '') + 'daily_active.csv'
    total_file_path = abs_file_path.replace(abs_file_path.split('/')[-1], '') + 'daily_cases.csv'
    deaths_file_path = abs_file_path.replace(abs_file_path.split('/')[-1], '') + 'daily_deaths.csv'

    df1 = pd.read_csv(total_file_path)
    df1.columns = map(str.lower, df1.columns)
    dates = list(df1['date'])
    total_cases = list(df1[country.lower()])

    df1 = pd.read_csv(active_file_path)
    df1.columns = map(str.lower, df1.columns)
    active_cases = list(df1[country.lower()])

    df1 = pd.read_csv(deaths_file_path)
    df1.columns = map(str.lower, df1.columns)
    deaths_cases = list(df1[country.lower()])

    # recovered = total - active
    recovered_cases = list(map(int.__sub__, total_cases, active_cases))
    # recovered = recovered - deaths
    recovered_cases = list(map(int.__sub__, recovered_cases, deaths_cases))

    active_dict = []
    recovered_dict = []
    deaths_dict = []

    for i in range(len(dates)):
        active_dict.append({'label' : dates[i], 'y' : active_cases[i]})
        recovered_dict.append({'label' : dates[i], 'y' : recovered_cases[i]})
        deaths_dict.append({'label' : dates[i], 'y' : deaths_cases[i]})

    return {
        'active' : active_dict,
        'recovered' : recovered_dict,
        'deaths' : deaths_dict
    }