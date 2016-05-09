# XSS/CSRF Challenge 1

----------------------

Hey mate. I have a few things I need your help checking out.

First, I've heard complaints about our user profiles being broken. Apparently, some users are getting logged out when they visit certain user profiles. One security-astute user said it had something to do with a simple CSRF attack. Can you look into this and see if you can duplicate it?

The relevant pages are likely the Preferences page and the My Profile page. You can view other user's profiles by going to Explore, then User List, then clicking a person's name. You'll need to register a new account to get into the game.

-Breakthenet Game Owner

----------------------

Stuck? 
----------------------
<details> 
  <summary>Click for hint 1</summary>
   When a webpage loads an image, your cookies/logged in session is passed to the server on which the image is hosted. 
</details>

<details> 
  <summary>Click for hint 2</summary>
  If you load a non-image url into an html image tag... html still makes the request to that url with the user's cookies, and the user just sees a broken image.
</details>

<details> 
  <summary>Click for hint 3</summary>
   What happens if you try putting a non-image url into the Display Pic preference? 
</details>



