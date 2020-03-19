from flask import Flask, request, redirect
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
        print(name, email, country)
        insert_to_db(name,email,country)
        view_subs()
        return redirect('http://localhost:3000/subscribed=yes')

if __name__ == '__main__':
    app.run(debug = True)