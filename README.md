# TextSpammer
 Use Twilio's REST API to spam text messages
 <br/>
 <br/>
 <br/>
 ## Setup:
 * Register on [Twilio.com](https://www.twilio.com/), purchase a number, and add funds to your account.
 <br/>
 <br/>
 * Add your SID and Token to the configuration file.
 <br/>
 ```INI
[CREDS]
SID = Your SID
TOKEN = Your Token
NUMBER = Twilio phone number
``` 

* Run the program and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser, or host it on the web.

## Notes:

1. By default, the max quantity of messages is 100. You can edit the index.html to be whatever you want. Twilio's limit is 4hrs or 14,400 messages. So have fun!
2. It's ugly, be warned.
3. I suck at programming so expect issues. 