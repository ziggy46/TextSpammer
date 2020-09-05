from flask import Flask, request, render_template
from twilio.rest import Client
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=["POST"])
def some_function():
    account_sid = config['CREDS']['SID']
    auth_token = config['CREDS']['TOKEN']
    text = request.form.get('phonenumber')
    msg = request.form.get('message')
    qty = request.form.get('times')
    client = Client(account_sid, auth_token)

    for _ in range(int(qty)):
        message = client.messages.create(
            to="+1" + text,
            from_="+1" + config['CREDS']['NUMBER'],
            body=msg)

        print(message.sid)

    return index()


if __name__ == '__main__':
    app.run()
