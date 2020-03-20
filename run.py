from flask import Flask, request, redirect, url_for
from db_conns import *

app = Flask(__name__)

@app.route('/subscribe', methods = ['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        print('reached here!')
        result = request.form
        name = result['name']
        email = result['email']
        country = result['country']
        # validate input here!!
        print(name, email, country)
        insert_to_db(name,email,country)
        print(get_subs())
    absolute_url = url_for('subscribe', _external = True)
    ind = absolute_url.rfind('subscribe')
    ind = ind - 5   # port number ka 4 digit and / => 5
    new_url = absolute_url[:ind] + '3000'
    print(new_url)
    return redirect(new_url)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)