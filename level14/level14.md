# SnowCrash Level14 Guide
This guide will walk you through the process of finding the password for the `flag14` user.

## Procedure:

1. **Examine your environment**
   
`id` : Shows user and group identities that you have. 
```bash
uid=2014(level14) gid=2014(level14) groups=2014(level14),100(users)
```
`pwd` : Displays the current directory you are in.
```bash
/home/user/level14
```
`ls -la` : Lists files and their permissions in the current directory.
Nothing interesting here.

We will now look at the files belonging to the user `flag14`, `level14` and the group `level14`.
```bash
find / -user flag14 2>/dev/null
find / -user level14 2>/dev/null
find / -groups level14 2>/dev/null
```
But we don't find anything interesting.
```bash
~$ ls -ls /var/mail/
4 -rw-r--r--+ 1 root mail 58 May 14 10:26 level05
```
Even after a lot of searching, we can't find anything...

2. **Analyse getflag**

The only executable we have is `/bin/getflag`.
So, we will decompile it using `gdb` to understand how it works.
```bash
gdb /bin/getflag
```
Returns
```bash
GNU gdb (Ubuntu/Linaro 7.4-2012.04-0ubuntu2.1) 7.4-2012.04
Copyright (C) 2012 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i686-linux-gnu".
For bug reporting instructions, please see:
<http://bugs.launchpad.net/gdb-linaro/>...
Reading symbols from /bin/getflag...(no debugging symbols found)...done.
```
The `dissasemble` gdb command she allows us to see the assembly code of a function.
```bash
(gdb) disassemble main
```
Returns
```bash
0x08048adc <+406>:	mov    $0x804906c,%eax
0x08048ae1 <+411>:	mov    %edx,0xc(%esp)
...
0x08048afd <+439>:	call   0x80484b0 <getuid@plt>
...
0x08048b0f <+457>:	je     0x8048ccb <main+901>
0x08048b15 <+463>:	cmp    $0xbbe,%eax
0x08048b1a <+468>:	ja     0x8048b68 <main+546>
```
There is lot of assembly code here, but we can see that the program is checking the return value of `getuid`, as in the previous levels.
Maybe it's a protection to prevent us from running the program as `flag14`.

3. **Exploit getflag with gdb**

So we will try to get the `flag14` user's UID.
```bash
id flag14
```
Returns
```bash
uid=3014(flag14) gid=3014(flag14) groups=3014(flag14),1001(flag)
```
As in the previous levels, we will use `gdb` to change the return value of `getuid` to `3014`.
```bash
(gdb) break getuid
Breakpoint 1 at 0x80484b0
(gdb) run
Starting program: /bin/getflag 
You should not reverse this
[Inferior 1 (process 3270) exited with code 01]
```
The programm exited with code 01 and the message `You should not reverse this`, there is protection against debugging and reverse engineering.
Indeed, the program is using the `ptrace` function to detect if it is being debugged.
```bash
0x0804897a <+52>:	movl   $0x0,0x4(%esp)
0x08048982 <+60>:	movl   $0x0,(%esp)
0x08048989 <+67>:	call   0x8048540 <ptrace@plt>
0x0804898e <+72>:	test   %eax,%eax
```

4. **Bypass ptrace**

We can bypass this by setting the return value of `ptrace` to 0.
```bash
(gdb) catch syscall ptrace
Catchpoint 1 (syscall 'ptrace' [26])
```
The command above set a catchpoint on the `ptrace` syscall.
```bash
(gdb) commands 1
```
The command above will execute the following commands when the catchpoint is hit. 1 is the error code of the `ptrace` syscall.
```bash
>set ($rax) = 0
>continue
>end
```
`$rax` is used to store the return value of the syscall.
The command above will set the return value of the `ptrace` syscall to 0. We make believe that the check of the `ptrace` function was successful.

5. **Change the return value of getuid**

Now we can try to change the return value of `getuid` to `3014`, again.
```bash
(gdb) break getuid
Breakpoint 2 at 0x80484b0
(gdb) run
Starting program: /bin/getflag 

Catchpoint 1 (call to syscall ptrace), 0xb7fdd428 in __kernel_vsyscall
    ()

Catchpoint 1 (returned from syscall ptrace), 0xb7fdd428 in __kernel_vsyscall ()

Breakpoint 2, 0xb7ee4cc0 in getuid ()
   from /lib/i386-linux-gnu/libc.so.6
(gdb) print $eax
$1 = 32
```
Here, `$eax == 32`. Our UID is `2014`, so we continue the execution of the program with one step.
```bash
(gdb) step
Single stepping until exit from function getuid,
which has no line number information.
0x08048b02 in main ()
(gdb) print $eax
$2 = 2014
```
We have the return value of `getuid` in the `$eax` register. We can change it to `3014`.
```bash
(gdb) set $eax = 3014
(gdb) print $eax
$3 = 3014
```
Now we can continue the execution of the program.
```bash
(gdb) continue
Continuing.
Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
[Inferior 1 (process 3336) exited normally]
```

Congratulations! We have succeeded in obtaining the token!
