# Setup Mailgun

----------------------

In this walkthrough, we will setup mailgun to receive emails and forward them to our api call for processing.

----------------------

Open [Twilio's website](https://www.twilio.com/) and create an account. You'll need to top it up with around $10.

Navigate to Hash symbol -> Manage Numbers -> Active Numbers
![](http://teachthe.net/topclipbox/2016-05-14_00-10-4643OKW6.png)

Hit plus to buy a number with voice and SMS.

Once purchase, you'll want to configure it like so:
![](http://teachthe.net/topclipbox/2016-05-14_00-11-57Z52DRU.png)

Where the Voice->"A call comes in" is (replace the base with your heroku url):
```
http://tranquil-escarpment-79784.herokuapp.com/catch_phone_call
```

And the Messaging->"A message comes in" is (replace the base with your heroku url):
```
http://tranquil-escarpment-79784.herokuapp.com/catch_sms
```

Hit save.

Now write down your phone number. In my images above, it was (314) 441-3417.

Go to Heroku -> Your app -> Settings -> Reveal Config Vars

![](http://teachthe.net/topclipbox/2016-05-14_00-13-34PBWT3V.png)

Scroll down until you can add a new value

![](http://teachthe.net/topclipbox/2016-05-14_00-14-01MJ2ZLF.png)

Set it like so:

![](http://teachthe.net/topclipbox/2016-05-14_00-14-36TDMF1G.png)

Where the value is YOUR Twilio #.

Hit save and you are done.