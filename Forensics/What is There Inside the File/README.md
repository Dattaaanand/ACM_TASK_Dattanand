# Trybreakingme.zip Broken
### So previously, I had done this task using John the ripper and one of my friends told that I had to use a python script to open it so I made the changes.

- I went to google and searched for a wordlist of passwords, and took a file from a github repository.
- Then I found a python script that could check all the passwords from wordlist and extract Trybreakingme.zip.
- So I created a python virtual environment from where I could install pyzipper, and run zipopen.py script to crack the password.
- The password obtained was 'softball3'.
- Then the extracted file "Unopenable og.pdf" was obtained whose contents could not be read directly.
- So I used evince pdf viewer and got the base64 code as "Rm9yZW5zaWNzIGlzIGZ1bg==".
- I decoded this base64 code using cyberchef and terminal and got the final text as "Forensics is fun".
