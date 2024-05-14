# SnowCrash Level13 Guide
This guide will walk you through the process of finding the password for the `flag13` user.

## Procedure:

1. **Examine your environment**
   
`id` : Shows user and group identities that you have. 
```bash
uid=2013(level13) gid=2013(level13) groups=2013(level13),100(users)
```
`pwd` : Displays the current directory you are in.
```bash
/home/user/level13
```
`ls -la` : Lists files and their permissions in the current directory.
```bash
-rwsr-sr-x 1 flag13 level13 7303 Aug  30  2015 level13
```
We have a binary file, `level13`.

2. **Analyse level13**

We execute the binary.
```bash
./level13
```
Returns
```bash
UID 2013 started us but we we expect 4242
```
We can see that the binary is checking the UID of the user running it. Our UID is 2013, but the binary expects 4242.
We can use `ltrace` to see what the binary is doing.
```bash
ltrace ./level13
```
We can see that the binary is calling `getuid()` to get the UID of the user running it.
Now, we can change our UID to 4242, or we can make believe that our program that our UID is 4242.

3. **Debug level13 with GDB**

We can use GDB to debug the binary.
```bash
gdb ./level13
```
Now in GDB, we want to change the return value of `getuid()` to 4242. So we set a breakpoint at the `getuid()` function and change the return value.
```bash
(gdb) break getuid
Breakpoint 1 at 0x8048380
(gdb) run
Starting program: /home/user/level13/level13 

Breakpoint 1, 0xb7ee4cc0 in getuid ()
   from /lib/i386-linux-gnu/libc.so.6
```
In the x86 architecture, the return value of a function is stored in the `eax` register. We can change the value of `eax` to 4242.
```bash
(gdb) print $eax
$1 = 1
```
We are currently before the `getuid()` function is called.
```bash
(gdb) step
Single stepping until exit from function getuid,
which has no line number information.
0x0804859a in main ()
(gdb) print $eax
$2 = 2013
```
We have the return value of `getuid()` in the `eax` register. We can change it to 4242.
```bash
(gdb) set $eax = 4242
(gdb) print $eax
$3 = 4242
```
Now we can continue the execution of the program.
```bash
(gdb) continue
Continuing.
your token is 2A31L79asukciNyi8uppkEuSx
[Inferior 1 (process 2927) exited with code 050]
(gdb) quit
```

Congratulations! We have succeeded in obtaining the token!
We now access level 14.
```bash
su level14
```