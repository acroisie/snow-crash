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

3. **Analyze the script to understand its workings.**
   
   - It is a simple Perl web-based application, which is indicated to be run locally on port 4747.
   - It uses the CGI Perl module to capture the 'x' parameter from an HTTP request, interpreted as a shell command and is executed irrespective of its content.
   - However, the script does no sanitation or filtering of the input, making it a classic example of a command injection vulnerability.
   - This vulnerability could be potentially exploited by a malicious user to execute arbitrary commands.

4. **Use a web browser to execute the script with a carefully crafted input string.**
   
   - Open a web browser and navigate to the following URL: `http://XXX.XXX.XX.XX:4747/?x=$(getflag)`
   - This input string bypasses the filter and executes the getflag command, which displays the flag.

5. **The flag should be displayed in the web browser.**
   
   - If the exploit was successful, the flag should be displayed in the web browser.
   - Record the flag for later use.