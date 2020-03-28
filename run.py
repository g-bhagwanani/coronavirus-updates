from flask import Flask, request, redirect, url_for
from db_conns import *
import re
import json
from aux_functions import get_details_of
from aux_functions import send_welcome_mail
from flask_cors import cross_origin

app = Flask(__name__)
# CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

def valid_mail(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex, email):
        return True
    else:
        return False

@app.route('/subscribe', methods = ['GET', 'POST'])
def subscribe():
    message = ''
    country = 'world'
    if request.method == 'POST':
        print('reached here!')
        result = request.form
        print(result)
        name = result['name']
        email = result['email']
        country = result['country']
        # validate input here!!
        print(name, email, country)
        if '' in [name, email, country]:
            message = 'incomplete'
        elif not valid_mail(email):
            message = 'wrongemail'
        else:
            message = 'subscribed'
            try:
                insert_to_db(name,email,country)
            except:
                message = 'issue'
            send_welcome_mail(name, email, country)
        print(message)
        try:
            print(get_subs())
        except:
            pass
    absolute_url = url_for('subscribe', _external = True)
    ind = absolute_url.rfind('subscribe')
    ind = ind - 5   # port number ka 4 digit and / => 5
    if message == 'subscribed':
        new_url = absolute_url[:ind] + '3000/stats/' + country.lower()
    else:
        new_url = absolute_url[:ind] + '3000/home/' + message
    print(new_url)
    return redirect(new_url)

@app.route('/getinfo', methods = ['GET'])
@cross_origin()
def getinfo():
    print(request.args)
    country = request.args.get('country')
    if country:
        if country == 'world':
            country = 'total:'
        print(country)
        values = get_details_of(country)
        print(values)
        keys = ['Total Cases', 'Active Cases', 'Recovered', 'Total Deaths']
        vals = [values[0], values[5], values[4], values[2]]
        extras = [values[7], str(round(values[5]*100/values[0], 2)) + '%', str(round(values[4]*100/values[0], 2)) + '%', str(round(values[2]*100/values[0], 2)) + '%']
        extra_texts = ['cases per million population', 'of total cases', 'of total cases', 'of total cases']
        country_info = []
        for i in range(len(keys)):
            country_info.append({'title': keys[i], 'value': vals[i], 'extra_val': extras[i], 'extra_text': extra_texts[i]})
        print(country_info)
        return json.dumps(country_info)
    else:
        return 'not allowed'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)