# CLI Help

## find
Search for files based on parameters.

```bash
find . -name "*.txt"
```
Searches all files in the current folder and subfolders.

```bash
find / -type d -name "docs"
```
Searches for folders named "docs" starting from the root of the system.

```bash
find / -size +100M
```
Searches all files larger than 100M starting from the root of the system.

```bash
find / -type f -name "*.tmp" -exec rm {} \;
```
Executes the rm command on all .tmp files.

```bash
find / -type f -perm -111
```
Searches all files executable by the owner, group, and others.

```bash
find / -user 'user1'
```
Searches all files belonging to user1.

## ls -l

```bash
ls -l
```
Displays:
```bash
-rwsr-sr-x 1 flag00 level00 8627 Mar  5  2016 level00
```
- -rwsr-sr-x : file permissions
- the first character is the file type
- the next three are the owner's permissions
- the next three are the group's permissions
- the next three are others' permissions
- possible permissions: rwx (read, write, execute)
- s : setuid, setgid : executes the file with the owner's or group's rights
- 1 : number of symbolic links pointing to the file
- flag00 : file owner
- level00 : file group
- 8627 : file size
- Mar  5  2016 : date of last modification
- level00 : file name

## strings

```bash
strings /bin/ls
```
Displays the printable character strings in the file.

```bash
strings /bin/ls | grep "usage"
```
Searches for the word "usage" within the output.

## which

```bash
which ls
```
Displays the absolute path of the ls command.

## export

```bash
export PATH=$PATH:/home/user/bin
```
Adds /home/user/bin to the PATH, affecting any program launched from this shell.

## printenv

```bash
printenv
```
Displays all the environment variables.

## id

```bash
id
```
Displays the current user's identifier and the groups the user belongs to.

## groups

```bash
groups
```
Displays the groups the current user belongs to.

## nc

```bash
nc [options] [hostname] [port]
```
Netcat is a versatile networking tool used for reading from and writing to network connections using TCP or UDP.
```bash
nc 127.0.0.1 5151
```

## curl

```bash
curl [options] [URL]
```
Curl is used to transfer data from or to a server, supporting protocols like HTTP, HTTPS, FTP, and more.
```bash
curl localhost:4646/?x=ARG
```

## egrep

```bash
egrep "a" /tmp/xd
```
Extended grep that searches a file for a pattern and outputs the matching lines, supports extended regular expressions.

## gdb

```bash
gdb program
```
GDB is the GNU Project debugger, allowing you to see what is going on 'inside' another program while it executes or what another program was doing at the moment it crashed.
