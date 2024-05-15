# SnowCrash Level09 Guide
This guide will walk you through the process of finding the password for the `flag09` user.

## Procedure:

1. **Examine your environment**
   
`id` : Shows user and group identities that you have. 
```bash
uid=2009(level09) gid=2009(level09) groups=2009(level09),100(users)
```
`pwd` : Displays the current directory you are in.
```bash
/home/user/level09
```
`ls -la` : Lists files and their permissions in the current directory.
```bash
-rwsr-sr-x 1 flag09 level09 7640 Mar  5  2016 level09
----r--r-- 1 flag09 level09   26 Mar  5  2016 token
```

2. **Analyse token**

We examine the file token.
```bash
cat token
```
Returns
```bash
f4kmm6p|=�p�n��DB�Du{��
```
We try to access at the flag09 user.
```bash
su flag09
Password:
```
Returns
```bash
su: Authentication failure
```
The token seems to be encrypted.

3. **Analyse level09**

We execute the file level09.
```bash
./level09
```
Returns
```bash
You need to provied only one arg.
```
We try to execute the file with different arguments.
```bash
./level09 a
a
./level09 b
b
./level09 abc
ace
./level09 test
tfuw
```
With the token:
```bash
./level09 'f4kmm6p|=pnDBDu{'
f5mpq;vEyxONQ
```
We try to access at the flag09 user with this token.
```bash
su flag09
Password:
```
Returns
```bash
su: Authentication failure
```
The token seems to be encrypted by ./level09.
We are going to decrypt it.

4. **Understand the algorithm used to encrypt the token**

After some tests, we find that the token is encrypted with the following algorithm:
Each character of the argument is incremented by the position of the character in the argument.
```bash
./level09 abcdef
acegik
```
```
a -> a + 0 = a
b -> b + 1 = c
c -> c + 2 = e
d -> d + 3 = g
e -> e + 4 = i
f -> f + 5 = k
```

5. **Create a python script to decrypt the token**

We are going to write a python script to decrypt the token.
We don't have the right to write in the current directory, so we are going to write the script in /tmp.
```python
#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        msg = sys.argv[1]
        decrypted_msg = ""
        for i, char in enumerate(msg):
                decrypted_msg += chr(ord(char) - i)
        print(decrypted_msg)
```
`ord` returns the Unicode code of a character.
`chr` returns the character of a Unicode code.

6. **Decrypt the token**

We use the python script to decrypt the token.
```bash
python /tmp/decrypt.py `cat token`
```
Returns
```bash
f3iji1ju5yuevaus41q1afiuq
```
We try to acces at the flag09 user with this token.
```bash
su flag09
Password:
```
Returns
```bash
Don't forget to launch getflag !
```
We execute the getflag command.
```bash
getflag
```
Returns
```bash
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
```

Congratulations! We have succeeded in obtaining the token!
We now access level 10.
```bash
su level10
```