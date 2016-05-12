# Setup Mailgun

----------------------

In this walkthrough, we will setup mailgun to receive emails and forward them to our api call for processing.

----------------------

Open Heroku, click your app.

On the Resources tab, click Mailgun
![](http://teachthe.net/topclipbox/click_mailgun.png)

Click Routes
![](http://teachthe.net/topclipbox/2016-05-10_13-46-35RLF30T.png)

Click Create New Route
![](http://teachthe.net/topclipbox/2016-05-10_13-48-06KPA4N0.png)

New Route Details:
![](http://teachthe.net/topclipbox/2016-05-10_13-47-31W2U5IV.png)

Filter Expression = `catch_all()`

Actions = `forward("http://hm-spoof.herokuapp.com/catch_email")`
*Replace hm-spoof.herokuapp.com with your heroku app's url.

Hit save, and you're done!
