# Social Engineering Challenges

These challenges require a user to successfully spoof emails, clone website login forms, spoof sms, spoof caller id to get into voicemail, and the like. It is recommended to have Kali installed in a VM to have all the tools available you need to complete them.

SETUP:
----------------------

###Step 1

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

*NOTE - if you get an error while deploying, wait 60 seconds and try again. The phantomjs buildpack used in this deploy fails intermittently on build when heroku has trouble establishing a connection to bitbucket, but it's always worked for me after a couple tries.

###Step 2

[Configure Mailgun](https://github.com/breakthenet/HackMe-Social-Engineering-Challenges/blob/master/setup/mailgun.md)

###Step 3 (Optional, involves Paid Services)

- Only required for optional Challenges 4 and 5
- Requires an account on a paid service, Twilio to setup.
- Also requires people to use paid accounts to solve with sms/voice spoofing providers.
- [Configure Twilio](https://github.com/breakthenet/HackMe-Social-Engineering-Challenges/blob/master/setup/twilio.md)


Challenges:
----------------------

[Challenge 1](https://github.com/breakthenet/HackMe-Social-Engineering-Challenges/blob/master/challenges/challenge_1.md): Spoof an email with your own custom reply-to.

[Challenge 2](https://github.com/breakthenet/HackMe-Social-Engineering-Challenges/blob/master/challenges/challenge_2.md): Spoof an email with linked phishing site, harvest credentials.

[Challenge 3](https://github.com/breakthenet/HackMe-Social-Engineering-Challenges/blob/master/challenges/challenge_3.md): Spoof an email with booby-trapped attachment that opens a reverse shell session. 

[Optional: Challenge 4](https://github.com/breakthenet/HackMe-Social-Engineering-Challenges/blob/master/challenges/challenge_4.md): Spoof an SMS (using a paid service), asking person to change a password on something as their boss. 

[Optional: Challenge 5](https://github.com/breakthenet/HackMe-Social-Engineering-Challenges/blob/master/challenges/challenge_5.md): Spoof a phone call's caller ID (using a paid service), use to retrieve voicemail.

----------------------

Note that useful information for testing and debugging will be logged to the Papertrail app in your heroku instance. Open papertrail to view those streaming logs.
