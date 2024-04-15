# SnowCrash Level04 Guide
This guide will walk you through the process of finding the password for the `flag04` user.

## Procedure:

1. **Examine your environment using Unix commands.**
   
   - `id` : Shows user and group identities that you have. 
   - `pwd` : Displays the current directory you are in.
   - `ls -la` : Lists files and their permissions in the current directory.
  
2. **After executing `ls -la`, you should notice a file called 'level04.pl'.**

   - The file is a Perl script that runs with the privileges of the flag04 user.
   - It takes input from the user and executes it as a system command.

3. **Analyze the script to determine how to exploit it.**
   - The script takes input from the user and passes it to the system function, which executes it as a command.
   - However, the script filters out certain characters to prevent users from executing arbitrary commands.
   - To exploit the script, you need to find a way to bypass the filter and execute a command that will display the flag.

4. **Use a web browser to execute the script with a carefully crafted input string.**
   - Open a web browser and navigate to the following URL: `http://192.168.64.4:4747/?x=$(getflag)`
   - This input string bypasses the filter and executes the getflag command, which displays the flag.

5. **The flag should be displayed in the web browser.**
   - If the exploit was successful, the flag should be displayed in the web browser.
   - Record the flag for later use.