# Social Engineering Challenge 2

----------------------

Great job on that last one, it went great. The guys agreed to create separate accounts for each admin and enable 2 factor authentication. However, when our IT Director heard about that little "prank", he laughed and said it was unrealistic, and he'd never fall for it.

We'll see. I've got a new challenge for you. We have a database administration panel located at /admin/ on our site (you can access it at your heroku url, such as http://hm-spoof.herokuapp.com/admin/). As you can see, there is a login screen there.

I'd like you to send a spoofed email to our IT Director, Scotty LaForge. Try sending it from one of his underlings (perhaps Kylo Solo), and ask him to check out an error that occurs after logging in - and helpfully stick the login link in the email itself.

Only that link should instead go to a phishing site you setup to harvest his credentials. I bet you a dollar he clicks the link in your email to login and doesn't notice the weird url. Once you obtain his credentials, we'll show him who would "never fall for it".

Frank Johnson (Chief Security Officer, Veritas Inc.)

NOTE - Scotty LaForge is notorious for clicking links in emails. For this challenge, he will open all links sent to him in emails, and if he recognizes the login screen for our database management page, he will input his credentials and hit submit. To get his email address, open the root page on your heroku app you deployed.

----------------------

Stuck? 
----------------------
<details> 
  <summary>Click for hint 1</summary>
  The social engineering toolkit has a setting that lets you exactly clone a website, and then capture any post requests sent through the form. You'll find it under SET's options Social-Engineering Attacks -> Website Attack Vectors -> Credential Harvester Attack Method -> Site Cloner. Note that if you use this, it will start an apache server for you on port 80. To expose that to the outside world, you can download ngrok and run `./ngrok http 80`. (Note that the ngrok url is what you'll want to use for the "IP address for the POST back in Harvester" setting in SET).
</details>

<details> 
  <summary>Click for hint 2</summary>
  Did you know you can send html emails via sendEmail? It's a bit hard to find via a google search, but it would look like this:
  
  ```
  -m "Here is a link <a href='http://google.com'>Click here</a> -Emeth" -o message-content-type=html
  ```
  
  Where "-m" gives your email message, and "-o message-content-type=html" makes the email be correctly formatted to be read as an html email in email clients.

</details>

