import os
import pandas as pd
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = 'coronavirusupdates2910@gmail.com'
sender_pw = 'Covid19Coronavirus'
website_url = 'http://ec2-13-126-87-109.ap-south-1.compute.amazonaws.com'

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
