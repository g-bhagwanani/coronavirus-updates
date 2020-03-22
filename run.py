from flask import Flask, request, redirect, url_for
from db_conns import *
import re

app = Flask(__name__)

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
            insert_to_db(name,email,country)
        print(message)
        print(get_subs())
    absolute_url = url_for('subscribe', _external = True)
    ind = absolute_url.rfind('subscribe')
    ind = ind - 5   # port number ka 4 digit and / => 5
    if message == 'subscribed':
        new_url = absolute_url[:ind] + '3000/stats/' + country.lower()
    else:
        new_url = absolute_url[:ind] + '3000/home/' + message
    print(new_url)
    return redirect(new_url)

# country stats thing!
@app.route('/countrystats', methods = ['GET', 'POST'])
def countrystats():
    stats_key = 'world'
    if request.method == 'POST':
        result = request.form
        print(result)
        stats_key = result['country'].lower()
    print(stats_key)
    absolute_url = url_for('subscribe', _external = True)
    ind = absolute_url.rfind('subscribe')
    ind = ind - 5   # port number ka 4 digit and / => 5
    new_url = absolute_url[:ind] + '3000/stats/' + stats_key
    print(new_url)
    return redirect(new_url)
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)