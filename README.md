# XSS/CSRF Challenges

These challenges are set in a Text-Based 'MM'ORPG Game based off Mccode Lite Game Engine (GPL)

Deploy to your own Heroku instance with this button below, then complete the challenges!

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

*NOTE - if you get an error while deploying, wait 60 seconds and try again. The phantomjs buildpack used in this deploy fails intermittently on build when heroku has trouble establishing a connection to bitbucket, but it's always worked for me after a couple tries.


Challenges:
----------------------

[Challenge 1](https://github.com/breakthenet/xss-exercises/blob/master/challenges/challenge_1.md): Basic CSRF

[Challenge 2](https://github.com/breakthenet/xss-exercises/blob/master/challenges/challenge_2.md): XSS - thinking outside the box

[Challenge 3](https://github.com/breakthenet/xss-exercises/blob/master/challenges/challenge_3.md): CSRF - trick an admin into upgrading your account to admin status.

[Challenge 4](https://github.com/breakthenet/xss-exercises/blob/master/challenges/challenge_4.md): XSS via BBCode parser, steal admin's cookies

[Challenge 5](https://github.com/breakthenet/xss-exercises/blob/master/challenges/challenge_5.md): XSS - creating a xss javascript worm

----------------------

Note that useful information for testing and debugging will be logged to the Papertrail app in your heroku instance. Open papertrail to view those streaming logs.
