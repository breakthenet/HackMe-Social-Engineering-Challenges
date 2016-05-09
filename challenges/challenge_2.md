# XSS/CSRF Challenge 2

Yikes. Thanks for finding that thing in Challenge 1. To get around that issue, I'm experimenting with a file-upload feature (instead of linking to an image url).

It's located at Preferences Preferences: Challenge 2 in the main menu of the game. Now you can upload a file there, and then see it in the user's profile.

Can you see if you can do something malicious with this?

-Breakthenet Game Owner

----------------------

Stuck? 
----------------------
<details> 
  <summary>Click for hint 1</summary>
   Keep in mind, everything that a user can control needs to be sanitized. Is there anything that the user can control here that we are displaying in the profile but not sanitizing from XSS/CSRF attacks?
</details>

<details> 
  <summary>Click for hint 2</summary>
   In this case, we are displaying both the user's image AND the image's file name. What can be stuck in the filename?
</details>

<details> 
  <summary>Click for hint 3</summary>
   While the Windows operating system is very restrictive about what characters can be in a filename, both OS X and Linux are much more forgiving. In fact, you can put html in a filename! For example... you could try something like [this](https://github.com/breakthenet/tools-and-techniques/blob/master/tools/%3Csvg%20onload%3Dalert(1)%3E.jpg).
</details>



