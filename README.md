# Social Engineering Challenges

These challenges require a user to successfully spoof emails, clone website login forms, spoof sms, spoof caller id to get into voicemail, and the like. It is recommended to have Kali installed in a VM to have all the tools available you need to complete them.

Deploy to your own Heroku instance with this button below. Once deployed, finish the configuration by opening the app in your browser.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

*NOTE - if you get an error while deploying, wait 60 seconds and try again. The phantomjs buildpack used in this deploy fails intermittently on build when heroku has trouble establishing a connection to bitbucket, but it's always worked for me after a couple tries.


Challenges:
----------------------

[Challenge 1](https://github.com/breakthenet/HackMe-Social-Engineering-Challenges/blob/master/challenges/challenge_1.md): Spoof an email with your own custom reply-to.

[Challenge 2](https://github.com/breakthenet/HackMe-Social-Engineering-Challenges/blob/master/challenges/challenge_2.md): Spoof an email with linked phishing site, harvest credentials.

[Challenge 3](https://github.com/breakthenet/HackMe-Social-Engineering-Challenges/blob/master/challenges/challenge_3.md): Spoof an email with booby-trapped pdf attachment that grants shell access. [TO BE WRITTEN]

[Challenge 4](https://github.com/breakthenet/HackMe-Social-Engineering-Challenges/blob/master/challenges/challenge_4.md): Spoof an SMS, ask person to set password to something. [TO BE WRITTEN]

[Challenge 5](https://github.com/breakthenet/HackMe-Social-Engineering-Challenges/blob/master/challenges/challenge_5.md): Spoof a phone call's caller ID (using spoofcard), use to retrieve voicemail [TO BE WRITTEN]

----------------------

Note that useful information for testing and debugging will be logged to the Papertrail app in your heroku instance. Open papertrail to view those streaming logs.
