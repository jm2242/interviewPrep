# Linux

## Linux Interview Questions

### How to check what kernel version you're running?

`$ uname -a`

Prints all system information



### How to check what your IP address?

`$ ifconfig` -> appanrelty this is the old way


### How to check for free disk space?

`$ df -ah`


### How would see if a service is running?

`$ systemctl status [service name]`

### Check the total size of a given directory?

`$ du -sh [path]`

### Check for open ports?

`$ netstat `


### How to check % CPU usage

A few ways:

`$ top `

or 

`$ ps aux | grep [processName`

### Dealing with Mounts

How would you mount a hard drive or USB?

`$ mount /dev/sda2 /mnt` will mount volume `/dev/sda2` on `/mnt`






