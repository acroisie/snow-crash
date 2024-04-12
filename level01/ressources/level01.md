## SnowCrash Level01 Guide
This guide will walk you through the process of finding the password for the `flag01` user.

## Procedure

1. **Examine your environment using Unix commands.**
   
    - `id` : Shows user and group identities. 
    - `pwd` : Displays the current directory you're in. 
    - `ls -la` : Lists files and their permissions in the current directory.
  
2. **Use 'grep' to search for specific user information in the `/etc/passwd` file.**
    - `cat /etc/passwd | grep flag01` : This command searches the filesystem for any information belonging to `flag01` in the `/etc/passwd` file.
    The `/etc/passwd` file is where Unix stores user information, including the hashed passwords.

3. **Extract the encrypted password and the username.**
   
    - The result of the previous command is: `flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash`
    - Here, `flag01` is the username and `42hDRfypTqqnw` is the hashed password.

4. **Create a text file with the hashed password and the username.**
    
    - Create a new text file (let's say `hash.txt`) and save the username and the hash in it, in the format `flag01:42hDRfypTqqnw`.

5. **Use John the Ripper to decrypt the password.**

    - John the Ripper is a popular password cracking software that can be used to crack passwords using various hashing algorithms.
    - Now run the command `john hash.txt`
    - John the Ripper will use its built-in dictionary to try and crack the password.
    
6. **View the decrypted password.**
    - Once John the Ripper has successfully cracked the password, run the command `john --show hash.txt` to view the password. This command will display the username and the decrypted password.

7. **Access `flag01`.**
    - Use `su flag01` and input the decrypted password when prompted.
    - You should now have access to the `flag01` account!

This is a straightforward process that uses basic Unix/Linux commands along with a password-decrypting attempt using John the Ripper to find the password.