# SnowCrash Level08 Guide
This guide will walk you through the process of finding the password for the `flag08` user.

## Procedure:

1. **Examine your environment using Unix commands.**

   - `id` : Shows user and group identities that you have.
   - `pwd` : Displays the current directory you are in.
   - `ls -la` : Lists the files and their permissions in the current directory.

2. **After executing `ls -la`, you should notice two files called 'level08' and 'token'.**

   - The file 'level08' is an executable that runs with the privileges of the flag08 user.
   - The 'token' file is a file whose content will be displayed by the executable, as long as the filename given as a parameter does not contain the word "token".

3. **Try to read the token file with the program.**

   - Execute the `level08` program with 'token' as a parameter using the command `./level08 token`.
   - The program outputs "You may not access 'token'", indicating a restriction based on the file name.

4. **Analyze the details of the program.**

   - Use the command `strings level08` to display readable sequences of characters in the executable. You should see the string "You may not access '%s'", which matches the output when you tried to read the token file.
   - Use the command `ltrace ./level08 token` to track dynamic library calls made by the program. It shows that 'strstr' function is blocking access to anything with the word "token".

5. **Create a symbolic link to the 'token' file and execute the program with this link as a parameter.**

   - Open a terminal and navigate to the temporary directory with the command `cd /tmp`.
   - Create a symbolic link to the 'token' file with the command `ln -s ~/token /tmp/my_file`.
   - Execute the `level08` program with the symbolic link as a parameter using the command `./level08 /tmp/my_file`. 