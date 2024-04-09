# SnowCrash Level00 Guide
This guide will walk you through the process of finding the password for the `flag00` user.

## Procedure

1. **Examine your environment using Unix commands.**
   
    - `id` : Shows user and group identities. 
    - `pwd` : Displays the current directory you're in. 
    - `ls -la` : Lists files and their permissions in the current directory.
    
2. **Use 'find' to search for user-specific files.**

    - `find / -user level00` and `find / -user flag00 2>/dev/null`: 
      These commands search the filesystem for any files belonging to `level00` and `flag00` respectively. The `2>/dev/null` part suppresses error messages. 
   Find is a versatile command for searching files based on criteria like owner, permissions, type, size, etc. Here, it's being used to find a potential lead to the `flag00` password.

3. **Inspect and decipher them.**

    - Run `cat /usr/sbin/john` and `cat /rofs/usr/sbin/John`. 
    - Collect the output: 

        ```shell
        cdiiddwpgswtgt
        ```

4. **Decrypt the output.**

    - Paste `cdiiddwpgswtgt` in Google. A Caesar cipher decoder link from dcode.fr will appear.
    - Use the decoder and get `nottoohardhere`. This Caesar cipher, also known as a shift cipher, works by shifting the letters in the alphabet by a certain number of places.

5. **Access `flag00`.**

    - Use `su flag00` and input `nottoohardhere` when asked for password.
    - You can now access the `flag00` account!

This is a straightforward process that uses basic Unix/Linux commands combined with a simple Caesar cipher decryption to find the password.