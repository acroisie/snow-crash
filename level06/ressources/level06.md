# SnowCrash Level06 Guide
This guide will walk you through the process of finding the password for the `flag06` user.

## Procedure:

1. **Examine your environment using Unix commands.**

   - `id` : Shows user and group identities that you have.
   - `pwd` : Displays the current directory you are in.
   - `ls -la` : Lists files and their permissions in the current directory.

2. **After executing `ls -la`, you should notice two files called 'level06' and 'level06.php'.**

   - The file 'level06' is an executable that runs with the privileges of the flag06 user.
   - The file 'level06.php' is a PHP script that takes two parameters and calls a function to get the content of the first parameter, assuming it refers to a file.

3. **Analyze the script to determine how to exploit it.**
   - The PHP script uses the deprecated and vulnerable regex 'e' modifier.
   - The regex `/(\[x (.*)\])/e` will evaluate any string arranged in the form "[x (.*)]", interpret it as PHP code and call the 'y' function with ".*" as parameter.
   - To exploit the script, you need to find a way to inject code that will execute the getflag command.

4. **Create a temporary file with the injected code and execute the script with this file as a parameter.**
   - Open a terminal and navigate to the temporary directory with the command `cd /tmp`.
   - Create a temporary file with the command `echo '[x ${`getflag`}]' > /tmp/getflag`.
   - Execute the level06 script with the command `./level06 /tmp/getflag`.

5. **The flag should be displayed in the terminal.**
   - If the exploit was successful, the flag should be displayed in the terminal.