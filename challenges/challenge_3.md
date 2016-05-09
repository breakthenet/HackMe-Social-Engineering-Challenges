# XSS/CSRF Challenge 3

----------------------

Hey friend,

I recently added profile signatures to user profiles (due to popular demand from my users). These signatures can be set under the Preferences page, and support BBCode.

My profile signatures are such a hit, I gave them to a friend - a guy who runs another game like mine (based off the same game engine).

He told me he got "hacked" - he said he was browsing through user profiles, and came across one that had a link in his profile signature. He clicked the link, and when he went back to the game, he found that user was suddenly an admin! He still has no idea how it happened.

Perhaps you could dig into it and shed some light on it? As far as we know, the only way to change a user's status is via the Staff Panel -> Adjust User Level form, which looks like [this](https://github.com/breakthenet/xss-exercises/blob/master/new_staff_actions.php#L1455-L1483).

I have a phantomjs bot setup that will log in as my admin account and visit all user profiles in the game. Then, for each profile, it will click ANY links in each profile signature (you can create a link in bbcode with `[url]http://site.com[/url]`). To trigger this bot, just go to Trigger Admin Browser in the navigation. 

Thanks!

-Breakthenet Game Owner

----------------------

Stuck? 
----------------------
<details> 
  <summary>Click for hint 1</summary>
   The simpler way to complete this challenge is to host an html page somewhere else on the internet, and stick a link to it on your profile signature. The admin bot will eventually click on it, and you can trigger your javascript payload on that external site within the context of the admin's browser.
</details>

<details> 
  <summary>Click for hint 2</summary>
   There is no CSRF token on the [form used in the admin panel](https://github.com/breakthenet/xss-exercises/blob/master/new_staff_actions.php#L1455-L1483) to update a user's admin status! This means you can try a CSRF attack! Try to get the admin's browser to submit that form for you. In whatever solution you come up with, compare it to the code linked above very closely, since that is what you are trying to emulate. If needed, you can get your user ID from the Explore -> User List page.
</details>

<details> 
  <summary>Click for hint 3</summary>
   Try googling "how to create and submit a form dynamically in javascript". There are some good stackoverflow examples.
</details>



