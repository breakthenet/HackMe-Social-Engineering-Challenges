# Spoof Challenge 1

----------------------

Hey mate. Thanks for your help with that pentest a few weeks back.

I have a new challenge for you. I wish to educate the management team here at Veritas Inc. on the severity of social engineering attacks.

Bob Dole is our CEO. Ted Jones is his CFO. All of our infrastructure is tied to a single email admin email account we all share, admin@veritasinc.com. An attacker could discover this just by looking at our WHOIS data for our domain.

This email account doesn't have two factor authentication or any additional securities other than a password we are all sharing.

I want you to social engineer the password off Bob Dole, our CEO. You should send him an email, making it appear to be from Ted Jones (the CFO). Ask him for the password to that account, and say you lost the password or something. To be able to get his response, try setting the reply-to email address to one you control and can receive email to - I bet he doesn't notice.

- Frank Johnson
Chief Security Officer, Veritas Inc.

----------------------

Stuck? 
----------------------
<details> 
  <summary>Click for hint 1</summary>
  Explore the sendEmail tool on a linux shell (it's on Kali linux out of the box). 
</details>

<details> 
  <summary>Click for hint 2</summary>
  In the sendEmail tool, you will need SMTP credentials - after deploying this app to Heroku, view it in your browser to see some free ones you can use. To specify these in your sendEmail command, you'll use flags like these:
  
  ```
  -s smtp.sendgrid.net:587 -xu app5059@heroku.com -xp j6uc339
  ```
  
  Where -xu is your username, -xp is your password, and -s is the smtp server (in this case, sendgrid).
</details>

<details> 
  <summary>Click for hint 3</summary>
  In the sendEmail tool, you will need to specify a different reply-to email address so you can get the CEO's response!
  
  ```
  -t to@email.com -f from@email.com -o reply-to=mypersonalemail@gmail.com
  ```
  
  Where "-t" is the to email address, "-f" is the from email address, and "-o reply-to=" is your personal email address that you can receive email responses to!
</details>
